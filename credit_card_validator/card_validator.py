"""
Class that handle all the validations for credit_card_validator
"""
import json
from dataclasses import asdict
from functools import lru_cache
from typing import List

from credit_card_validator.exceptions import LuhnUnsupportedEception
from credit_card_validator.exceptions import NoBrandFoundException
from credit_card_validator.schemas import CardBrand
from credit_card_validator.schemas import CardOut


class _CardValidator:
    """
    All functions related to finding a card brand from a number
    """

    def __init__(self):
        self.card_brands: List[CardBrand] = []

        with open(
            "./credit_card_validator/card_brands.json", "r", encoding="utf-8"
        ) as file:
            data_imported = json.load(file)
            for brand in data_imported["card_brands"]:
                self.card_brands.append(CardBrand(**brand))

    def _card_brand(self, card_number: str) -> CardBrand:
        """
        Parse the card brand list and find matching brand associated with card number
        :param card_number: self-explanatory
        :return: brand object
        """

        number_size = len(card_number)
        for brand in self.card_brands:
            for rule in brand.card_rules:
                for size in rule.card_lengths:
                    if number_size == size:
                        for prefix in rule.card_prefixs:
                            if card_number.startswith(prefix):
                                return brand
        raise NoBrandFoundException(f'No brand found for card number "{card_number}"')

    def _is_luhn_valid(
        self, number: str, skip_brand_finder: bool = False, brand: CardBrand = None
    ) -> bool:
        """
        Verify if mod10 (luhn) algorithm valid the card number
        Don't use this function directly, it returns false for card brand that do not follow luhn algorithm
        :param number: Card numbers in str format
        :param skip_brand_finder: only try luhn algorithm (can be false negative)
        :return: True
        """

        if not skip_brand_finder and CardBrand is None:
            card_brand = brand if brand is not None else self._card_brand(number)
            if card_brand.skip_luhn:
                raise LuhnUnsupportedEception(
                    f"card brand {card_brand.brand_name} doesn't support luhn algorithm"
                )

        reg = [int(ch) for ch in number][::-1]
        return (
            sum(reg[0::2]) + sum(sum(divmod(digit * 2, 10)) for digit in reg[1::2])
        ) % 10 == 0

    def card_brands_to_dict(self) -> List[dict]:
        """
        Return a user friend brands validation list
        :return: List of brands
        """

        brands: List[dict] = []
        for brand in self.card_brands:
            brands.append(asdict(brand))
        return brands

    def _brand(self, card_number: str) -> CardBrand:
        """
        Parse the card brand list and find matching brand associated with card number
        :param card_number: self-explanatory
        :return: brand name
        """

        brand: CardBrand = self._card_brand(card_number)
        if brand:
            return brand

    def card_verified(
        self,
        card_number: str,
    ) -> CardOut:
        """
        verify card information
        :param card_number: self-explanatory
        :return: CardOut object
        """

        luhn_valid = None
        try:
            brand = self._brand(card_number)
            if not brand.skip_luhn:
                luhn_valid = self._is_luhn_valid(card_number, brand=brand)

        except NoBrandFoundException:
            brand = CardBrand("Unknown", "unknown", [])

        return CardOut(
            brand.skip_luhn, card_number, brand.brand_name, luhn_valid, brand.name
        )


@lru_cache()
def card_validator() -> _CardValidator:
    """
    A simple card validation library
    :return: A lru cached _CardValidator instance
    """
    return _CardValidator()
