"""Acceptance test for plan-shout-t1."""
from loopsample.textops import shout


def test_shout_uppercases_with_bang():
    assert shout("hello") == "HELLO!"
