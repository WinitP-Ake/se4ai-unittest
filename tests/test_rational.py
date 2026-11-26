"""Unit tests for rational.py.

Add your tests here: one or more for every public method of Rational,
designed with input space partitioning (see TEST_PLAN.md).
"""
from rational import Rational


def test_add():
    # Rational(1, 2) cannot be used yet: the constructor is part of your task.
    # So this test sets the numerator and denominator by hand.
    x = Rational()
    x.numerator, x.denominator = 1, 2
    y = Rational()
    y.numerator, y.denominator = 1, 4

    result = x.add(y)

    assert result.numerator == 3
    assert result.denominator == 4
