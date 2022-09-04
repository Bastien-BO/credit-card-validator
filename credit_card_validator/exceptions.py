"""
All exceptions and errors classes
"""


class PycardException(BaseException):
    """
    Global exception for credit_card_validator
    """


class NoBrandFoundException(PycardException):
    """
    Raise if credit_card_validator was unable to find a related card brand
    """


class LuhnUnsupportedEception(PycardException):
    """
    Raise if luhn algorithm tried but card brand doesn't support it
    """
