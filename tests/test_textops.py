"""Tests for loopsample.textops."""

from loopsample.textops import truncate


class TestTruncate:
    def test_short_text_unchanged(self):
        assert truncate("abc", 10) == "abc"

    def test_exactly_at_limit_unchanged(self):
        assert truncate("abcde", 5) == "abcde"

    def test_long_text_is_cut_and_marked(self):
        result = truncate("abcdefghij", 5)
        assert result.endswith("…")
        assert result.startswith("abc")
