"""
All schemas to represent card brands
"""
from dataclasses import dataclass
from typing import List
from typing import Union


@dataclass
class CardRules:
    """
    card rules representation
    """

    card_lengths: List[int]
    card_prefixs: List[str]


@dataclass
class CardBrand:
    """
    Representation of a Card brand
    """

    brand_name: str
    name: str
    card_rules: List[Union[dict, CardRules]]
    skip_luhn: bool = False

    def __post_init__(self):
        card_rules: List[CardRules] = []
        for elem in self.card_rules:
            card_rules.append(CardRules(**elem))
        self.card_rules = card_rules


@dataclass
class CardOut:
    """
    Representation of the card data output
    """

    luhn_skipped: bool
    number: str
    brand_name: str = "Unknown"
    luhn_valid: bool = None
    name: str = "unknown"
