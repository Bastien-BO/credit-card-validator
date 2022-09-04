"""
All tests related to card brands
"""

from credit_card_validator.card_validator import card_validator


def test_card_validator_loading():
    """
    test if the validator is well created
    """
    validator = card_validator()
    assert validator is not None


def test_card_brands_loading():
    """
    test if the brands list is well created
    """
    validator = card_validator()
    brands = validator.card_brands_to_dict()
    assert brands is not None
