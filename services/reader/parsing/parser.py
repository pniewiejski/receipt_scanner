"""
Parse receipt data
"""

# from receipt import Receipt
# from parsing_strategies.only_sum import only_sum

from parsing.receipt import Receipt
from parsing.parsing_strategies.only_sum import only_sum
from parsing.parsing_strategies.shop_sum import shop_sum

def select_stategy(text, default=False):
    """
    Returns a parsing strategy (function).
    """
    #func = only_sum
    func = shop_sum
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
