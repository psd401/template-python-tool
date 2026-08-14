"""Tests for psd_tool.text.slugify.

Real assertions with exact expected values (05-testing.md): empty input,
unicode, truncation, and both error paths are covered.
"""

import pytest

from psd_tool import slugify


def test_basic_sentence() -> None:
    assert slugify("Peninsula School District") == "peninsula-school-district"


def test_strips_accents_and_folds_case() -> None:
    assert slugify("Café MÜNCHEN") == "cafe-munchen"


def test_collapses_punctuation_and_whitespace_runs() -> None:
    assert slugify("  hello --- world!!  ") == "hello-world"


def test_empty_and_symbol_only_input_yield_empty_slug() -> None:
    assert slugify("") == ""
    assert slugify("!!! ???") == ""


def test_truncates_without_trailing_separator() -> None:
    # "alpha-beta"[:6] is "alpha-"; the trailing separator must be stripped.
    assert slugify("alpha beta", max_length=6) == "alpha"


def test_exact_fit_is_not_truncated() -> None:
    assert slugify("alpha beta", max_length=10) == "alpha-beta"


def test_custom_separator() -> None:
    assert slugify("a b c", separator="_") == "a_b_c"


def test_rejects_max_length_below_one() -> None:
    with pytest.raises(ValueError, match="max_length"):
        slugify("anything", max_length=0)


def test_rejects_multi_character_separator() -> None:
    with pytest.raises(ValueError, match="separator"):
        slugify("anything", separator="--")
