import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculadora import soma

def test_soma():
    assert soma(2, 3) == 5
