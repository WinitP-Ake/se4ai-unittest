# Test plan for `Rational`

Name:

For each method, list the **characteristics** of its inputs, split each one into **blocks** (partitions), and pick the test values. Blocks of one characteristic must not overlap, and together they must cover every possible input. The first row is an example.

## Constructor `Rational(numerator, denominator)`

| Characteristic | Blocks | Test values (numerator, denominator) → expected |
|---|---|---|
| sign of the denominator | negative · zero · positive | (1, -2) → -1/2 · (1, 0) → `IllegalRationalError` · (1, 2) → 1/2 |
| sign of the numerator | | |
| | | |

## `add`, `subtract`, `multiply`, `divide`

| Characteristic | Blocks | Test values (x, y) → expected |
|---|---|---|
| | | |

## `==` (`__eq__`)

| Characteristic | Blocks | Test values → expected |
|---|---|---|
| | | |

## `compare_to`

| Characteristic | Blocks | Test values → expected |
|---|---|---|
| | | |

## `str` (`__str__`)

| Characteristic | Blocks | Test values → expected |
|---|---|---|
| | | |
