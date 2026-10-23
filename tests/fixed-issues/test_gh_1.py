"""Regression test for gh-1: truncate must respect the limit."""
from loopsample import truncate


def test_truncate_respects_limit():
    result = truncate("abcdefghij", 5)
    assert len(result) <= 5, f"truncate returned {len(result)} characters"
    assert result == "abcd…"
