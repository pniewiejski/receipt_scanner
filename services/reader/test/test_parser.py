"""
Test parser module
"""
import pytest

TEXT = ""
EXPECT = ""

@pytest.mark.parametrize(('text', 'expect'), [
    (TEXT, EXPECT)
])
def test_strategy_selection(text: str, expect: str):
    assert 1 == 1
