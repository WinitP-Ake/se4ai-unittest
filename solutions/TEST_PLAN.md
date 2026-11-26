# Test plan for `Rational` (one possible answer)

Other characteristics and blocks can be just as good. What matters is that the blocks of each characteristic do not overlap, cover every input, and that each block has at least one test. The tests are in [`test_rational.py`](test_rational.py).

## Constructor `Rational(numerator, denominator)`

| Characteristic | Blocks | Test values (numerator, denominator) → expected |
|---|---|---|
| sign of the denominator | negative · zero · positive | (1, -2) → -1/2 · (1, 0) → `IllegalRationalError` · (1, 2) → 1/2 |
| sign of the numerator | negative · zero · positive | (-1, 2) → -1/2 · (0, 5) → 0/1 · (1, 2) → 1/2 |
| form of the fraction | simplest · reducible · whole number | (1, 2) → 1/2 · (2, 4) → 1/2 · (6, 3) → 2/1 |
| arguments given | none · numerator only · both | () → 0/1 · (3,) → 3/1 · (1, 2) → 1/2 |
| type of the arguments | int · not int | (1, 2) → 1/2 · (0.5, 1), (1, 2.0), ("1", 2) → `TypeError` |

Combinations worth a test of their own: both negative (-2, -4) → 1/2, and zero with a negative denominator (0, -5) → 0/1.

## `add`, `subtract`, `multiply`, `divide`

| Characteristic | Blocks | Test values (x, y) → expected |
|---|---|---|
| signs of x and y | both positive · one negative · both negative | add (1/2, 1/4) → 3/4 · subtract (1/4, 3/4) → -1/2 · multiply (-1/2, -2/3) → 1/3 |
| y is zero | yes · no | add (2/3, 0) → 2/3 · multiply (2/3, 0) → 0 · divide (1/2, 0) → `ZeroDivisionError` |
| form of the result | zero · whole number · reducible fraction | add (1/2, -1/2) → 0 · add (1/2, 1/2) → 1 · subtract (3/4, 1/4) → 1/2 |
| order of x and y (subtract, divide) | x > y · x < y | subtract (3/4, 1/4) → 1/2 · subtract (1/4, 3/4) → -1/2 |
| operands after the call | unchanged | x = 1/2, y = 1/3 are still 1/2 and 1/3 after each method |

## `==` (`__eq__`)

| Characteristic | Blocks | Test values → expected |
|---|---|---|
| type of the other value | Rational · not a Rational | 1/2 == 0.5, "1/2", None → `False` |
| how the values relate | same value, same form · same value, other form · different value | 1/2 == 1/2 → `True` · 1/2 == 2/4 → `True` · 1/2 == 1/3 → `False` |
| what the different values share | same numerator · same denominator · opposite sign | 1/2 vs 1/3 · 1/3 vs 2/3 · 1/2 vs -1/2 → `False` |

## `compare_to`

| Characteristic | Blocks | Test values → expected |
|---|---|---|
| how x and y relate | x < y · x == y · x > y | (1/3, 1/2) → -1 · (1/2, 2/4) → 0 · (1/2, 1/3) → 1 |
| signs of x and y | both positive · mixed · both negative · zero | (-1/2, 1/3) → -1 · (-1/2, -1/3) → -1 · (0, -1/5) → 1 |
| size of the difference | small · large | (3, 5/2) → 1 (the result is 1, not the difference) |

## `str` (`__str__`)

| Characteristic | Blocks | Test values → expected |
|---|---|---|
| sign | negative · zero · positive | -3/4 → "-3/4" · 0/7 → "0" · 3/4 → "3/4" |
| whole number | yes · no | 5/1 → "5" · -4/2 → "-2" · 1/2 → "1/2" |
| as given | simplest · reducible · negative denominator | 2/4 → "1/2" · 3/-4 → "-3/4" |
