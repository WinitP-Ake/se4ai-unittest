"""One possible test suite for Rational, designed with input space partitioning.

Characteristics used (see solutions/TEST_PLAN.md):
  sign of the numerator     negative | zero | positive
  sign of the denominator   negative | zero | positive
  form of the fraction      already simplest | reducible | whole number
  type of the inputs        int | not int
  relation of x and y       x < y | x == y | x > y
  the other operand         zero | not zero   (divide)
"""
import pytest

from rational import IllegalRationalError, Rational


def fields(r):
    return r.numerator, r.denominator


# ----------------------------------------------------------- constructor --

@pytest.mark.parametrize("args, expected", [
    ((), (0, 1)),          # default is zero
    ((3,), (3, 1)),        # whole number
    ((1, 2), (1, 2)),      # positive, already simplest
    ((2, 4), (1, 2)),      # reducible
    ((-1, 2), (-1, 2)),    # negative numerator
    ((1, -2), (-1, 2)),    # negative denominator: sign moves up
    ((-2, -4), (1, 2)),    # both negative, reducible
    ((0, 5), (0, 1)),      # zero numerator
    ((0, -5), (0, 1)),     # zero with a negative denominator
    ((6, 3), (2, 1)),      # reduces to a whole number
])
def test_constructor_stores_simplest_form(args, expected):
    assert fields(Rational(*args)) == expected


def test_constructor_rejects_zero_denominator():
    with pytest.raises(IllegalRationalError):
        Rational(1, 0)


@pytest.mark.parametrize("args", [(0.5, 1), (1, 2.0), ("1", 2)])
def test_constructor_rejects_non_integers(args):
    with pytest.raises(TypeError):
        Rational(*args)


# ------------------------------------------------------------ arithmetic --

@pytest.mark.parametrize("x, y, expected", [
    ((1, 2), (1, 4), (3, 4)),
    ((1, 2), (1, 2), (1, 1)),      # result is a whole number
    ((1, 2), (-1, 2), (0, 1)),     # result is zero
    ((-1, 3), (-1, 6), (-1, 2)),   # negative operands
    ((2, 3), (0, 1), (2, 3)),      # adding zero
])
def test_add(x, y, expected):
    assert fields(Rational(*x).add(Rational(*y))) == expected


@pytest.mark.parametrize("x, y, expected", [
    ((3, 4), (1, 4), (1, 2)),      # reduces
    ((1, 4), (3, 4), (-1, 2)),     # negative result: order matters
    ((1, 2), (1, 2), (0, 1)),      # zero result
    ((-1, 2), (-1, 3), (-1, 6)),
    ((2, 3), (0, 1), (2, 3)),
])
def test_subtract(x, y, expected):
    assert fields(Rational(*x).subtract(Rational(*y))) == expected


@pytest.mark.parametrize("x, y, expected", [
    ((2, 3), (3, 4), (1, 2)),      # reduces
    ((-1, 2), (1, 3), (-1, 6)),    # one negative
    ((-1, 2), (-2, 3), (1, 3)),    # both negative
    ((2, 3), (0, 1), (0, 1)),      # times zero
    ((2, 3), (3, 2), (1, 1)),      # whole-number result
])
def test_multiply(x, y, expected):
    assert fields(Rational(*x).multiply(Rational(*y))) == expected


@pytest.mark.parametrize("x, y, expected", [
    ((1, 2), (1, 4), (2, 1)),
    ((1, 2), (-1, 4), (-2, 1)),    # divisor negative: sign must end up on top
    ((-3, 4), (-3, 8), (2, 1)),
    ((0, 1), (2, 3), (0, 1)),      # zero divided by something
    ((2, 3), (4, 5), (5, 6)),
])
def test_divide(x, y, expected):
    assert fields(Rational(*x).divide(Rational(*y))) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Rational(1, 2).divide(Rational(0))


@pytest.mark.parametrize("method", ["add", "subtract", "multiply", "divide"])
def test_arithmetic_does_not_change_the_operands(method):
    x, y = Rational(1, 2), Rational(1, 3)
    getattr(x, method)(y)
    assert fields(x) == (1, 2)
    assert fields(y) == (1, 3)


# ---------------------------------------------------------- equality, order --

@pytest.mark.parametrize("x, y, expected", [
    ((1, 2), (1, 2), True),
    ((1, 2), (2, 4), True),        # same value, different form
    ((1, 2), (-1, -2), True),
    ((1, 2), (1, 3), False),       # same numerator
    ((1, 3), (2, 3), False),       # same denominator
    ((1, 2), (-1, 2), False),      # opposite sign
])
def test_equals(x, y, expected):
    assert (Rational(*x) == Rational(*y)) is expected


@pytest.mark.parametrize("other", [0.5, "1/2", None])
def test_not_equal_to_other_types(other):
    assert (Rational(1, 2) == other) is False


@pytest.mark.parametrize("x, y, expected", [
    ((1, 3), (1, 2), -1),
    ((1, 2), (1, 3), 1),
    ((1, 2), (2, 4), 0),
    ((-1, 2), (1, 3), -1),         # negative vs positive
    ((-1, 2), (-1, 3), -1),        # both negative
    ((0, 1), (-1, 5), 1),          # zero vs negative
    ((3, 1), (5, 2), 1),           # whole numbers
])
def test_compare_to(x, y, expected):
    assert Rational(*x).compare_to(Rational(*y)) == expected


# ------------------------------------------------------------------ text --

@pytest.mark.parametrize("args, expected", [
    ((1, 2), "1/2"),
    ((3, 4), "3/4"),
    ((-3, 4), "-3/4"),
    ((3, -4), "-3/4"),
    ((2, 4), "1/2"),
    ((5, 1), "5"),
    ((-4, 2), "-2"),
    ((0, 7), "0"),
])
def test_str(args, expected):
    assert str(Rational(*args)) == expected
