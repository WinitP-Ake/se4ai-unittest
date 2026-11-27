"""Bug hunt version 11: one planted bug. Do not read: it spoils the exercise.

Rational numbers (fractions) such as 1/2, -3/4 and 5.

A Rational is always stored in its simplest form:

* the numerator and denominator have no common factor (2/4 is stored as 1/2);
* the denominator is always positive (1/-2 is stored as -1/2);
* zero is stored as 0/1.

The arithmetic methods return a NEW Rational and never change the one they
are called on, so  x.add(y)  leaves x unchanged.

The class is complete. Your task is to write unit tests for it in
tests/test_rational.py: read the docstrings to know what each method must do.
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
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("numerator and denominator must be int")
        if denominator == 0:
            raise IllegalRationalError("denominator cannot be 0")
        self.numerator = numerator
        self.denominator = denominator
        self._simplest_form()

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
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def subtract(self, other):
        """Return self - other as a new Rational."""
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def multiply(self, other):
        """Return self * other as a new Rational."""
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def divide(self, other):
        """Return self / other as a new Rational.

        Raises ZeroDivisionError if other is zero.
        """
        if other.numerator == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        """x == y is True if x and y are the same number: Rational(1, 2) == Rational(2, 4).

        Comparing with anything that is not a Rational, such as 0.5, gives False.
        """
        if not isinstance(other, Rational):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self):
        """The fraction as text: "1/2", "-3/4". Whole numbers have no denominator: "5", "0", "-2"."""
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    print("This is the Rational class.")
