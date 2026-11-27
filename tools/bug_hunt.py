"""How good are your tests? Runs them against 11 versions of Rational with one planted bug each.

    python3 tools/bug_hunt.py

First, your tests run against a CORRECT Rational: they must all pass, or a
test expects something the specification does not say. Then they run
against each buggy version. A bug is CAUGHT when at least one test fails.
For each bug you miss, a hint tells you which case of the input
your tests do not cover yet.

This is mutation testing (lecture) with hand-made mutants. Do not read the
files in tools/bugs/: they would spoil the exercise.
"""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HINTS = {
    "bug01": "constructor: a denominator of zero",
    "bug02": "constructor: a negative denominator",
    "bug03": "constructor: a negative fraction that can be reduced",
    "bug04": "constructor: zero written with a denominator other than 1",
    "bug05": "subtract: does the order of the operands matter?",
    "bug06": "multiply: two ordinary fractions",
    "bug07": "divide: dividing by zero",
    "bug08": "divide: is the number it is called on still the same afterwards?",
    "bug09": "equality: same numerator, different denominator",
    "bug10": "equality: comparing with something that is not a Rational",
    "bug11": "str: whole numbers",
}


def run_tests(impl, show_failures=False):
    """Run the tests against the module `impl`. Returns True if all pass."""
    env = dict(os.environ, RATIONAL_IMPL=impl, PYTHONDONTWRITEBYTECODE="1")
    args = [sys.executable, "-m", "pytest", "tests", "-p", "no:cacheprovider", "-q"]
    if not show_failures:
        args += ["-x", "--no-header", "--tb=no"]
    else:
        args += ["--tb=line", "-rf"]
    result = subprocess.run(args, cwd=ROOT, env=env, capture_output=True, text=True)
    if show_failures and result.returncode != 0:
        lines = [line for line in result.stdout.splitlines() if line.startswith("FAILED")]
        print("\n".join("  " + line for line in lines))
    return result.returncode == 0


def main():
    print("Your tests against a correct Rational ...", end=" ", flush=True)
    if not run_tests("rational", show_failures=False):
        print("SOME FAIL\n")
        run_tests("rational", show_failures=True)
        print("\nThese tests expect something the specification (the docstrings in")
        print("rational.py) does not say. Fix them first, then run the bug hunt again.")
        return 1
    print("all pass.\n")

    caught, missed = [], []
    for bug in sorted(HINTS):
        if run_tests(f"tools.bugs.{bug}"):
            missed.append(bug)
            print(f"  {bug}  missed   hint: {HINTS[bug]}")
        else:
            caught.append(bug)
            print(f"  {bug}  caught")

    print(f"\nYour tests caught {len(caught)} of {len(HINTS)} bugs.")
    if missed:
        print("For each missed bug, add a test for the case in the hint.")
    else:
        print("Every planted bug was caught.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
