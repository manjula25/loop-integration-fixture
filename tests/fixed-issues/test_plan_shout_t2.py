"""Acceptance test for plan-shout-t2."""
from loopsample.textops import shout_all


def test_shout_all_shouts_every_word():
    assert shout_all(["hi", "yo"]) == ["HI!", "YO!"]
