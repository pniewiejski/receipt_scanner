import pytest

from parsing.strategies.only_sum import only_sum

# TEXT = "this is a test string SUMA: 44.20 lorem ipsum"
# EXPECT = 44.20

@pytest.mark.parametrize(('text', 'expect'), [
    ("this is a test string SUMA: 44.20 lorem ipsum", 44.20),
    ("this is a test string SUMA: 44,20 lorem ipsum", 44.20),
    ("this is a test string SUMA:\t 44,20 lorem ipsum", 44.20),
    ("this is a test string SUMA:\t\n 544,20 lorem ipsum", 544.20),
    ("this is a test string SUMA PLN 544,20 lorem ipsum", 544.20)
])
def test_strategy_selection(text: str, expect: str):
    receipt = only_sum(text)
    assert receipt.totalCost == expect
