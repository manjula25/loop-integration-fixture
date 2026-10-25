"""Regression test for gh-1: truncate() returned one character more than the limit."""
from loopsample import truncate


def test_truncate_result_fits_within_limit():
    result = truncate("abcdefghij", 5)
    assert len(result) <= 5, f"truncate returned {len(result)} characters"


def test_truncate_matches_issue_example():
    assert truncate("abcdefghij", 5) == "abcd…"


def test_truncate_matches_docstring_example():
    assert truncate("abcdef", 4) == "abc…"


def test_short_text_still_unchanged():
    assert truncate("abcde", 5) == "abcde"
    assert truncate("abc", 10) == "abc"
