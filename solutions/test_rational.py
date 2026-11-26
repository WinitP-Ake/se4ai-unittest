"""One possible test suite for Rational. It catches all 14 planted bugs.

The tests pick inputs from different groups: negative, zero and positive
numbers; fractions that are already simple, can be reduced, or are whole
numbers; and inputs the methods must reject.
"""
import pytest

from rational import IllegalRationalError, Rational


# ----------------------------------------------------------- constructor --

def test_default_is_zero():
    r = Rational()
    assert r.numerator == 0
    assert r.denominator == 1


def test_whole_number():
    r = Rational(3)
    assert r.numerator == 3
    assert r.denominator == 1


def test_simple_fraction():
    r = Rational(1, 2)
    assert r.numerator == 1
    assert r.denominator == 2


def test_fraction_is_reduced():
    r = Rational(2, 4)
    assert r.numerator == 1
    assert r.denominator == 2


def test_negative_numerator():
    r = Rational(-1, 2)
    assert r.numerator == -1
    assert r.denominator == 2


def test_negative_denominator_moves_sign_to_numerator():
    r = Rational(1, -2)
    assert r.numerator == -1
    assert r.denominator == 2


def test_negative_fraction_is_reduced():
    r = Rational(-2, 4)
    assert r.numerator == -1
    assert r.denominator == 2


def test_both_negative_gives_positive():
    r = Rational(-2, -4)
    assert r.numerator == 1
    assert r.denominator == 2


def test_zero_is_stored_as_zero_over_one():
    r = Rational(0, 5)
    assert r.numerator == 0
    assert r.denominator == 1


def test_zero_denominator_is_rejected():
    with pytest.raises(IllegalRationalError):
        Rational(1, 0)


def test_float_is_rejected():
    with pytest.raises(TypeError):
        Rational(0.5, 1)


# ------------------------------------------------------------ arithmetic --

def test_add():
    r = Rational(1, 2).add(Rational(1, 4))
    assert r.numerator == 3
    assert r.denominator == 4


def test_add_negative():
    r = Rational(-1, 3).add(Rational(-1, 6))
    assert r.numerator == -1
    assert r.denominator == 2


def test_subtract():
    r = Rational(3, 4).subtract(Rational(1, 4))
    assert r.numerator == 1
    assert r.denominator == 2


def test_subtract_larger_number_gives_negative():
    r = Rational(1, 4).subtract(Rational(3, 4))
    assert r.numerator == -1
    assert r.denominator == 2


def test_multiply():
    r = Rational(2, 3).multiply(Rational(3, 4))
    assert r.numerator == 1
    assert r.denominator == 2


def test_multiply_by_zero():
    r = Rational(2, 3).multiply(Rational(0))
    assert r.numerator == 0
    assert r.denominator == 1


def test_divide():
    r = Rational(2, 3).divide(Rational(4, 5))
    assert r.numerator == 5
    assert r.denominator == 6


def test_divide_by_negative():
    r = Rational(1, 2).divide(Rational(-1, 4))
    assert r.numerator == -2
    assert r.denominator == 1


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Rational(1, 2).divide(Rational(0))


def test_divide_does_not_change_the_operands():
    x = Rational(1, 2)
    y = Rational(1, 3)
    x.divide(y)
    assert x.numerator == 1 and x.denominator == 2
    assert y.numerator == 1 and y.denominator == 3


# ---------------------------------------------------------- equality, order --

def test_equal_to_same_value():
    assert Rational(1, 2) == Rational(2, 4)


def test_not_equal_with_same_numerator():
    assert Rational(1, 2) != Rational(1, 3)


def test_not_equal_with_opposite_sign():
    assert Rational(1, 2) != Rational(-1, 2)


def test_not_equal_to_a_float():
    assert (Rational(1, 2) == 0.5) is False


def test_compare_smaller():
    assert Rational(1, 4).compare_to(Rational(3, 4)) == -1


def test_compare_much_larger_still_gives_one():
    assert Rational(5).compare_to(Rational(1)) == 1


def test_compare_equal():
    assert Rational(1, 2).compare_to(Rational(2, 4)) == 0


def test_compare_negative_numbers():
    assert Rational(-1, 2).compare_to(Rational(-1, 3)) == -1


# ------------------------------------------------------------------ text --

def test_str_fraction():
    assert str(Rational(1, 2)) == "1/2"


def test_str_negative():
    assert str(Rational(3, -4)) == "-3/4"


def test_str_whole_number():
    assert str(Rational(5, 1)) == "5"


def test_str_zero():
    assert str(Rational(0, 7)) == "0"
