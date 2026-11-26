# Lets `pytest` import rational.py from the repository root.
#
# tools/bug_hunt.py sets RATIONAL_IMPL to run your tests against another
# implementation of Rational (for example one with a planted bug). Your tests
# still just write `from rational import Rational`.
import importlib
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

_impl = os.environ.get("RATIONAL_IMPL")
if _impl:
    sys.modules["rational"] = importlib.import_module(_impl)
