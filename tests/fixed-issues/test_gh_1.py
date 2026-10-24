"""Regression test for gh-1: truncate() returned one character more than the limit."""

from loopsample import truncate


def test_truncate_respects_the_limit():
    # Worked example from the issue: a 5-character budget must yield 'abcd…',
    # not 'abcde…' (which is 6 characters).
    assert truncate("abcdefghij", 5) == "abcd…"
    assert len(truncate("abcdefghij", 5)) == 5


def test_truncate_matches_docstring_example():
    # The docstring promises truncate("abcdef", 4) == "abc…" (three
    # characters plus the ellipsis, the ellipsis counting toward the limit).
    assert truncate("abcdef", 4) == "abc…"
