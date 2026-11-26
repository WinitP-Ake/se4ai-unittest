"""Rational numbers (fractions) such as 1/2, -3/4 and 5.

A Rational is always stored in its simplest form:

* the numerator and denominator have no common factor (2/4 is stored as 1/2);
* the denominator is always positive (1/-2 is stored as -1/2);
* zero is stored as 0/1.

The arithmetic methods return a NEW Rational and never change the one they
are called on, so  x.add(y)  leaves x unchanged.

This file is only partly written: the docstrings are the specification.
Write your tests from them FIRST, then complete the code.
"""
from math import gcd


class IllegalRationalError(ValueError):
    """Raised when a Rational would have a denominator of zero."""


class Rational:

    def __init__(self, numerator=0, denominator=1):
        """Create the rational number numerator/denominator.

        Rational() is 0, Rational(3) is 3, Rational(2, -4) is -1/2.

        Raises TypeError if numerator or denominator is not an int, and
        IllegalRationalError if denominator is 0.
        """
        # TODO: to be completed. Hint: _simplest_form() does the reducing for you.
        self.numerator = 0
        self.denominator = 1

    def _simplest_form(self):
        """Reduce the fraction and move the sign to the numerator."""
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common

    def add(self, other):
        """Return self + other as a new Rational."""
        result = Rational()
        result.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        result.denominator = self.denominator * other.denominator
        result._simplest_form()
        return result

    def subtract(self, other):
        """Return self - other as a new Rational."""
        # TODO: to be completed
        return Rational()

    def multiply(self, other):
        """Return self * other as a new Rational."""
        # TODO: to be completed
        return Rational()

    def divide(self, other):
        """Return self / other as a new Rational.

        Raises ZeroDivisionError if other is zero.
        """
        # TODO: to be completed
        return Rational()

    def __eq__(self, other):
        """x == y is True if x and y are the same number: Rational(1, 2) == Rational(2, 4).

        Comparing with anything that is not a Rational, such as 0.5, gives False.
        """
        # TODO: to be completed
        return True

    def __hash__(self):
        return hash((self.numerator, self.denominator))

    def compare_to(self, other):
        """Return -1 if self < other, 0 if self == other, 1 if self > other."""
        # TODO: to be completed
        return -1

    def __str__(self):
        """The fraction as text: "1/2", "-3/4". Whole numbers have no denominator: "5", "0", "-2"."""
        # TODO: to be completed
        return ""

    def __repr__(self):
        return f"Rational({self.numerator}, {self.denominator})"


if __name__ == "__main__":
    print("This is the Rational class.")
