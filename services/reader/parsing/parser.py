"""
Parse receipt data
"""

from receipt import Receipt
from parsing_strategies.only_sum import only_sum

def select_stategy(text, default=False):
    func = only_sum
    return func

def parse(text) -> str:
    """
    Parses raw text data according to an appropriate strategy

    Returns a JSON formated string
    """
    parser = select_stategy(text)
    receipt = parser(text)
    return receipt.to_json()

# if __name__ == "__main__":
#     print(parse("fdd"))

