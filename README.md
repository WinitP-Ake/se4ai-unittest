# Week 8 exercise: Unit tests for rational numbers

* CMKL 41-645 Software Engineering for AI-Enabled Systems
* Week 8: Quality Assurance Basics

**Individual homework · about 2 hours**

## Learning outcomes

By the end of this exercise, you should be able to:

1. Write unit tests with pytest: call, inputs, check, including expected exceptions.
2. Design test cases with **input space partitioning**: characteristics, blocks, and one test per block.
3. Practice **test-driven development**: write the tests first, then the code that makes them pass.
4. Judge the quality of a test suite by how many planted bugs it catches (mutation testing).

## Scenario

`rational.py` is a small class for **rational numbers** (fractions) such as `1/2`, `-3/4` and `5`:

```python
>>> from rational import Rational
>>> x = Rational(1, 2)
>>> y = Rational(1, 3)
>>> print(x.add(y))
5/6
>>> x.compare_to(y)
1
```

The class is only **partly written**. Its docstrings are the specification: what every method must do, including the unusual cases (a negative denominator, zero, a whole number). You will write the tests **first**, from the specification alone, and only then complete the class. This is **test-driven development (TDD)**.

| Method | What it does |
|---|---|
| `Rational(numerator=0, denominator=1)` | Creates a fraction and stores it in its simplest form. Raises `IllegalRationalError` for a zero denominator, `TypeError` for anything that is not an `int`. |
| `x.add(y)` | Returns `x + y` as a new `Rational`. **Already written.** |
| `x.subtract(y)`, `x.multiply(y)`, `x.divide(y)` | Return `x - y`, `x * y`, `x / y` as a new `Rational`. `divide` raises `ZeroDivisionError` when `y` is zero. |
| `x == y` | `True` if both are the same number, so `Rational(1, 2) == Rational(2, 4)`. |
| `x.compare_to(y)` | `-1`, `0` or `1`. |
| `str(x)` | `"1/2"`, `"-3/4"`, and for whole numbers just `"5"`, `"0"`. |

### The files

| File | What it is | Do you edit it? |
|---|---|---|
| `rational.py` | The `Rational` class. The docstrings are the specification. | **Yes**, in Step 5 only. |
| `tests/test_rational.py` | Your tests. One test, `test_add`, is already there. | **Yes**, Steps 3 and 4. |
| `TEST_PLAN.md` | Your input space partitioning, one table per method. | **Yes**, Step 2. |
| `tools/bug_hunt.py` | Runs your tests against 14 versions of `Rational` with one planted bug each. | No |
| `tools/bugs/` | The buggy versions. **Do not read them**: they spoil the exercise. | No |
| `solutions/` | A test plan, tests and a full `rational.py`, for when you are really stuck. **Try on your own first.** | No |
| `REFLECTION.md` | Three short questions. | **Yes**, at the end. |

---

## 0. Setup (10 min)

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
   It passes: `add` is already written. Open `tests/test_rational.py` and read `test_add`. Every unit test has the same parts: **call** the code, with some **inputs**, and **check** the result with `assert`.

> **Stuck?**
> - **Windows:** type `python` wherever this README says `python3` (after you activate the virtual environment).
> - Always run commands from the repository root (the folder with this README).
> - **VS Code:** the **Testing** panel (flask icon) runs single tests with a click, like the green arrow in IntelliJ.

---

## 1. Read the specification (10 min)

Open `rational.py` and read the module docstring and every method's docstring. Do not read the code yet; most of it is not written anyway.

Write down, for yourself, three inputs where you are **not sure** what a naive implementation would do. For example: what is `Rational(0, -5)`? What does `str()` give for it?

---

## 2. Partition the input space (25 min)

You cannot test every possible input, so you choose a few that represent all the others. **Input space partitioning** does this systematically:

1. List the **characteristics** of a method's inputs: properties that might change how the method behaves. For example, *the sign of the denominator*.
2. Split each characteristic into **blocks**: the blocks must not overlap, and together they must cover every possible input. For the sign of the denominator: *negative · zero · positive*.
3. Pick **one test value per block**, and work out the expected result **from the specification**: `Rational(1, -2)` is `-1/2`; `Rational(1, 0)` raises `IllegalRationalError`; `Rational(1, 2)` is `1/2`.
4. Combine characteristics where they might interact. Is `Rational(-2, -4)` handled correctly, where both are negative **and** the fraction can be reduced?

Fill in `TEST_PLAN.md`: one table per method. The first row is an example. Good characteristics to think about: signs, zero, whole numbers, fractions that can be reduced, the order of the operands, and inputs that are not what the method expects.

> **Stuck?**
> - Aim for 3 to 5 characteristics per method. More is not always better: every block needs a test.
> - "Not overlapping" means each input belongs to exactly one block. *negative · zero · positive* is fine; *negative · small · positive* is not.
> - For `x.subtract(y)`, the inputs are **two** fractions. Characteristics can be about one of them (*is `y` zero?*) or both (*is `x` larger than `y`?*).

---

## 3. Write the tests first (30 min)

Turn every row of your test plan into tests in `tests/test_rational.py`. Cover **every public method**: the constructor, `add`, `subtract`, `multiply`, `divide`, `==`, `compare_to` and `str`. **Do not change `rational.py` yet.**

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

@pytest.mark.parametrize("numerator, denominator, expected", [   # one test, many blocks
    (1, 2, "1/2"),
    (5, 1, "5"),
])
def test_str(numerator, denominator, expected):
    assert str(Rational(numerator, denominator)) == expected
```

Run them:

```bash
python3 -m pytest -v
```

Most of your tests **fail**: the code is not written yet. That is the point: in TDD, a new test must fail first ("red"). **But some of your tests probably pass.** Which ones, and why? Read the unfinished methods in `rational.py` to find out. Write it down for the reflection.

> **Stuck?**
> - Check `numerator` and `denominator` separately, or compare `str(r)`. Do not use `==` between two `Rational`s to check other methods: `==` is not written yet either, and the unfinished one always says `True`.
> - One test should check **one** thing. When it fails, its name should tell you what is wrong: `test_negative_denominator_moves_sign_to_numerator` beats `test_constructor_2`.
> - Arithmetic returns a **new** `Rational`. The specification says `x.add(y)` must leave `x` unchanged: that is testable too.

---

## 4. Hunt for bugs with your tests (20 min)

How do you know your tests are good? Run them against code that you **know** is wrong:

```bash
python3 tools/bug_hunt.py
```

The script first runs your tests against a **correct** `Rational`: they must all pass. If one fails, it expects something the specification does not say: fix that test. Then it runs your tests against **14 versions of `Rational` with one planted bug each**. A bug is **caught** when at least one of your tests fails on it.

```text
  bug01  caught
  bug02  missed   hint: constructor: a negative denominator
  ...
Your tests caught 11 of 14 bugs.
```

For every bug you miss, the hint names a block of the input space that your tests do not cover yet. Add that block to `TEST_PLAN.md`, add a test, and run the bug hunt again. **Aim to catch all 14.**

This is **mutation testing** from the lecture, with mutants written by hand: a test suite that catches more planted bugs is more likely to catch the real ones.

> **Stuck?**
> - Your tests pass against the correct `Rational` but fail on the unfinished `rational.py`? That is expected: the bug hunt does not use your `rational.py` at all.
> - Write down how many bugs your **first** bug hunt caught, for the reflection.

---

## 5. Make the tests pass (25 min)

Now, and only now, complete `rational.py`: every `# TODO`. Run the tests after each method:

```bash
python3 -m pytest -v
```

You are done when **every test passes** ("green"). If a test fails, decide which one is wrong, the code or the test, by reading the specification again.

> **Stuck?**
> - `_simplest_form()` reduces a fraction and moves the sign to the numerator. Call it at the end of the constructor.
> - `add` shows how the other arithmetic methods can work: build the result, then return it.
> - To compare `a/b` with `c/d` (with `b` and `d` positive), compare `a * d` with `c * b`.
> - Raise an exception with `raise IllegalRationalError("denominator cannot be 0")`.

---

## Push and submit (5 min)

Answer the three questions in [`REFLECTION.md`](REFLECTION.md), then commit and push:

```bash
git add -A
git commit -m "Test and implement Rational"
git push
```

> **Stuck?** If `git push` asks for a password, use the Codespace, GitHub Desktop, or sign in with `gh auth login`.

Submit the URL of your fork. Your fork should show:

- [ ] a complete `rational.py` that passes all your tests (`python3 -m pytest`);
- [ ] tests that catch as many planted bugs as you can (`python3 tools/bug_hunt.py`);
- [ ] `TEST_PLAN.md` with a table for every method;
- [ ] tests for every public method of `Rational`;
- [ ] `REFLECTION.md` filled in.

> [!WARNING]
> **Solutions are in [`solutions/`](solutions/README.md). Try each step on your own first.** Use the **Stuck?** tips and ask a classmate or the TA before you look.
