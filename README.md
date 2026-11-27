# Week 8 exercise: Unit tests for rational numbers

* CMKL 41-645 Software Engineering for AI-Enabled Systems
* Week 8: Quality Assurance Basics

**Individual in-class exercise · about 30 minutes**

## Learning outcomes

By the end of this exercise, you should be able to:

1. Write unit tests with pytest: call, inputs, check, including expected exceptions.
2. Choose test inputs that cover the different cases a method must handle.
3. Judge how good a set of tests is by how many planted bugs it catches.

## Scenario

`rational.py` is a small, finished class for **rational numbers** (fractions) such as `1/2`, `-3/4` and `5`:

```python
>>> from rational import Rational
>>> x = Rational(1, 2)
>>> y = Rational(1, 3)
>>> print(x.add(y))
5/6
>>> x == Rational(2, 4)
True
```

Your task is to **write unit tests** for it. The class is correct. But someone will change it one day, and your tests must catch their mistakes.

| Method | What it does |
|---|---|
| `Rational(numerator=0, denominator=1)` | Creates a fraction and stores it in its simplest form: `Rational(2, -4)` is `-1/2`. Raises `IllegalRationalError` for a zero denominator, `TypeError` for anything that is not an `int`. |
| `x.add(y)`, `x.subtract(y)`, `x.multiply(y)`, `x.divide(y)` | Return `x + y`, `x - y`, `x * y`, `x / y` as a **new** `Rational`; `x` does not change. `divide` raises `ZeroDivisionError` when `y` is zero. |
| `x == y` | `True` if both are the same number, so `Rational(1, 2) == Rational(2, 4)`. |
| `str(x)` | `"1/2"`, `"-3/4"`, and for whole numbers just `"5"`, `"0"`. |

| File | What it is | Do you edit it? |
|---|---|---|
| `rational.py` | The `Rational` class. Its docstrings say what each method must do. | No |
| `tests/test_rational.py` | Your tests. One test, `test_add`, is already there. | **Yes** |
| `tools/bug_hunt.py` | Runs your tests against 11 versions of `Rational` with one planted bug each. | No |
| `tools/bugs/` | The buggy versions. **Do not read them**: they spoil the exercise. | No |
| `solutions/` | One possible set of tests, for when you are really stuck. | No |
| `REFLECTION.md` | Two short questions. | **Yes**, at the end. |

---

## 0. Setup (5 min)

1. **Fork** this repository (top right on GitHub) into your own account.
2. Get a terminal with Python. Pick **one** option:
   - **Your machine** (Python 3.9 or newer):
     ```bash
     git clone https://github.com/<your-username>/se4ai-unittest.git
     cd se4ai-unittest
     python3 -m venv .venv            # Windows: py -m venv .venv
     source .venv/bin/activate        # Windows: .venv\Scripts\activate
     python3 -m pip install -r requirements.txt
     ```
   - **No Python installed?** On your fork, click **Code → Codespaces → Create codespace on main**. Everything is installed for you.
3. Run the test that is already there:
   ```bash
   python3 -m pytest -v
   ```
   Open `tests/test_rational.py` and read `test_add`. Every unit test has the same parts: **call** the code, with some **inputs**, and **check** the result with `assert`.

> **Stuck?**
> - **Windows:** type `python` wherever this README says `python3` (after you activate the virtual environment).
> - Always run commands from the repository root (the folder with this README).

---

## 1. Write tests (15 min)

Read the docstrings in `rational.py`, then add tests to `tests/test_rational.py`: at least one for **every public method** (the constructor, `add`, `subtract`, `multiply`, `divide`, `==` and `str`).

A test that only tries one easy input catches few bugs. For each method, ask: **which different cases must it handle?** Negative numbers, zero, fractions that can be reduced, whole numbers, and inputs it must reject.

Three pytest features help:

```python
import pytest
from rational import IllegalRationalError, Rational

def test_reduces_to_simplest_form():
    r = Rational(2, 4)
    assert r.numerator == 1
    assert r.denominator == 2

def test_zero_denominator_is_rejected():        # expect an exception
    with pytest.raises(IllegalRationalError):
        Rational(1, 0)

@pytest.mark.parametrize("numerator, denominator, expected", [   # one test, many inputs
    (1, 2, "1/2"),
    (5, 1, "5"),
])
def test_str(numerator, denominator, expected):
    assert str(Rational(numerator, denominator)) == expected
```

Run your tests often. They should all pass, because `rational.py` is correct:

```bash
python3 -m pytest -v
```

> **Stuck?**
> - A test fails? Then the test is wrong: read the method's docstring again.
> - Name each test after what it checks: `test_negative_denominator_moves_sign_to_numerator` beats `test_constructor_2`.
> - The arithmetic methods return a **new** `Rational` and must leave `x` unchanged. That is testable too.

---

## 2. Hunt for bugs with your tests (7 min)

Are your tests good? Run them against code that you **know** is wrong:

```bash
python3 tools/bug_hunt.py
```

The script runs your tests against **11 versions of `Rational` with one planted bug each**. A bug is **caught** when at least one of your tests fails on it:

```text
  bug01  caught
  bug02  missed   hint: constructor: a negative denominator
  ...
Your tests caught 8 of 11 bugs.
```

Write down how many bugs you caught the first time. Then, for each missed bug, read the hint, add a test for that case, and run the bug hunt again. **Aim to catch all 11.**

This is **mutation testing** from the lecture, with bugs planted by hand: tests that catch more planted bugs are more likely to catch real ones.

---

## Submit (3 min)

Answer the two questions in [`REFLECTION.md`](REFLECTION.md), then commit and push:

```bash
git add -A
git commit -m "Write unit tests for Rational"
git push
```

> **Stuck?** If `git push` asks for a password, use the Codespace, GitHub Desktop, or sign in with `gh auth login`.

Submit the URL of your fork. It should have:

- [ ] tests for every public method of `Rational`, all passing;
- [ ] tests that catch as many planted bugs as you can;
- [ ] `REFLECTION.md` filled in.

> [!WARNING]
> **A solution is in [`solutions/`](solutions/README.md). Try on your own first.** Use the hints from the bug hunt and ask a classmate or the TA before you look.
