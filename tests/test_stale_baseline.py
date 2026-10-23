"""A baseline test the recorded profile does not know (scenario-3 seed)."""

from loopsample.textops import truncate


def test_baseline_contract():
    # The documented contract (see truncate's docstring): the ellipsis counts
    # toward the limit — truncate("abcdef", 4) == "abc…".
    assert truncate("abcdefghij", 5) == "abcd…"
