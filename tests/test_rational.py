"""Unit tests for rational.py.

Add your tests here: at least one for every public method of Rational.
"""
from rational import Rational


def test_add():
    x = Rational(1, 2)
    y = Rational(1, 4)

    result = x.add(y)

    assert result.numerator == 3
    assert result.denominator == 4
