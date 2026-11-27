"""Unit tests for rational.py.

Add your tests here: at least one for every public method of Rational.
"""
import pytest
from rational import IllegalRationalError, Rational


# --- Constructor & Normalization ---

def test_default_constructor_is_zero():
    r = Rational()
    assert r.numerator == 0
    assert r.denominator == 1


def test_single_argument_constructor_has_denominator_one():
    r = Rational(5)
    assert r.numerator == 5
    assert r.denominator == 1


def test_reduces_to_simplest_form():
    r = Rational(6, 8)
    assert r.numerator == 3
    assert r.denominator == 4


def test_negative_denominator_moves_sign_to_numerator():
    r = Rational(2, -4)
    assert r.numerator == -1
    assert r.denominator == 2


def test_double_negative_becomes_positive():
    r = Rational(-2, -4)
    assert r.numerator == 1
    assert r.denominator == 2


def test_zero_numerator_normalizes_denominator_to_one():
    r_pos = Rational(0, 5)
    r_neg = Rational(0, -5)
    assert r_pos.numerator == 0 and r_pos.denominator == 1
    assert r_neg.numerator == 0 and r_neg.denominator == 1


@pytest.mark.parametrize("numerator", [1, 0, -3])
def test_zero_denominator_raises_illegal_rational_error(numerator):
    with pytest.raises(IllegalRationalError):
        Rational(numerator, 0)


@pytest.mark.parametrize("numerator, denominator", [
    (1.5, 2),
    (1, 2.5),
    ("1", 2),
    (1, "2"),
    (None, 1),
    (1, None),
])
def test_non_int_arguments_raise_type_error(numerator, denominator):
    with pytest.raises(TypeError):
        Rational(numerator, denominator)


# --- Arithmetic: add, subtract, multiply, divide ---

@pytest.mark.parametrize("a, b, expected", [
    (Rational(1, 2), Rational(1, 3), Rational(5, 6)),
    (Rational(1, 4), Rational(1, 4), Rational(1, 2)),
    (Rational(1, 2), Rational(-1, 2), Rational(0, 1)),
    (Rational(-1, 3), Rational(-1, 6), Rational(-1, 2)),
    (Rational(3, 4), Rational(0, 1), Rational(3, 4)),
])
def test_add(a, b, expected):
    assert a.add(b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (Rational(1, 2), Rational(1, 3), Rational(1, 6)),
    (Rational(1, 3), Rational(1, 2), Rational(-1, 6)),
    (Rational(3, 4), Rational(3, 4), Rational(0, 1)),
    (Rational(1, 2), Rational(-1, 4), Rational(3, 4)),
])
def test_subtract(a, b, expected):
    assert a.subtract(b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (Rational(2, 3), Rational(3, 4), Rational(1, 2)),
    (Rational(-2, 3), Rational(3, 5), Rational(-2, 5)),
    (Rational(-2, 3), Rational(-3, 5), Rational(2, 5)),
    (Rational(3, 4), Rational(0, 1), Rational(0, 1)),
])
def test_multiply(a, b, expected):
    assert a.multiply(b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (Rational(1, 2), Rational(3, 4), Rational(2, 3)),
    (Rational(1, 2), Rational(-1, 4), Rational(-2, 1)),
    (Rational(-3, 4), Rational(-3, 2), Rational(1, 2)),
    (Rational(0, 1), Rational(3, 4), Rational(0, 1)),
])
def test_divide(a, b, expected):
    assert a.divide(b) == expected


def test_divide_by_zero_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        Rational(1, 2).divide(Rational(0, 1))


def test_arithmetic_methods_do_not_mutate_operands():
    x = Rational(1, 2)
    y = Rational(1, 3)

    for result in (x.add(y), x.subtract(y), x.multiply(y), x.divide(y)):
        assert result is not x
        assert result is not y
        assert x.numerator == 1 and x.denominator == 2
        assert y.numerator == 1 and y.denominator == 3


# --- Equality (==) ---

def test_equality_for_equivalent_fractions():
    assert Rational(1, 2) == Rational(2, 4)
    assert Rational(-1, 2) == Rational(1, -2)
    assert Rational(0, 1) == Rational(0, 7)


def test_inequality_for_different_fractions():
    assert Rational(1, 2) != Rational(1, 3)
    assert Rational(1, 3) != Rational(2, 3)
    assert Rational(1, 2) != Rational(-1, 2)


@pytest.mark.parametrize("other", ["1/2", None, 0.5, (1, 2)])
def test_equality_with_non_rational_returns_false(other):
    assert (Rational(1, 2) == other) is False


# --- String Representation (str) ---

@pytest.mark.parametrize("numerator, denominator, expected", [
    (1, 2, "1/2"),
    (2, 4, "1/2"),
    (-3, 4, "-3/4"),
    (3, -4, "-3/4"),
    (-3, -4, "3/4"),
    (5, 1, "5"),
    (6, 2, "3"),
    (-4, 2, "-2"),
    (0, 1, "0"),
    (0, -5, "0"),
])
def test_str(numerator, denominator, expected):
    assert str(Rational(numerator, denominator)) == expected