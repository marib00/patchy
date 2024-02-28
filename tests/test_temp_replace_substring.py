from __future__ import annotations

import sys
from textwrap import dedent

import patchy.api


def test_context_manager():
    def sample() -> int:
        return 1234

    assert sample() == 1234
    with patchy.temp_replace_substring(sample, "return 1234", "return 5678"):
        assert sample() == 5678
    assert sample() == 1234


def test_decorator():
    def sample() -> int:
        return 3456

    @patchy.temp_replace_substring(sample, "return 3456", "return 7890")
    def decorated() -> None:
        assert sample() == 7890

    assert sample() == 3456
    decorated()
    assert sample() == 3456

