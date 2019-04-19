"""
Parse receipt data
"""

# from receipt import Receipt
# from parsing_strategies.only_sum import only_sum

from parsing.receipt import Receipt
from parsing.strategies.only_sum import only_sum
from parsing.strategies.orlen import orlen

def select_strategy(text, default=False):
    """
    Returns a parsing strategy (function).
    """
    # TODO : refactor select_strategy or get rid of it! 
    # func = only_sum # use only_sum as temporary mock 
    func = orlen
    return func

def parse(text) -> str:
    """
    Parses raw text data according to an appropriate strategy

    Returns a JSON formated string
    """
    parser = select_strategy(text)
    receipt = parser(text)
    return receipt.to_json()

if __name__ == "__main__":
    print(parse("this is a test string SUMA: 44.20 lorem ipsum"))
