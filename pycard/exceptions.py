"""
All exceptions and errors classes
"""


class PycardException(BaseException):
    """
    Global exception for pycard
    """


class NoBrandFoundException(PycardException):
    """
    Raise if pycard was unable to find a related card brand
    """


class LuhnUnsupportedEception(PycardException):
    """
    Raise if luhn algorithm tried but card brand doesn't support it
    """
