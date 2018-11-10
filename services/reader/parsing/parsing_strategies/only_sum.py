"""
Find only the SUM
"""
import re
from parsing.receipt import Receipt # relative import - life is full of zasadzkas
from parsing.parsing_strategies import comma_to_dot
from parsing.errors.parsing_error import ParsingException

def only_sum(text: str) -> Receipt:
    """
    Extract only the SUM value
    """
    #search_for = re.compile(r"SUMA:{0,1}\s*(\d[\.,]\d\d)", re.IGNORECASE)
    parsed = re.search(r"SUMA:{0,1}\s*(\d+[\.,]\d\d)", text, re.IGNORECASE)
    parsed = parsed.group(1)
    parsed = comma_to_dot(parsed)
    try:
        total_cost = float(parsed)
    except:
        #raise NotImplementedError("Not implemented parsing error")        
        raise ParsingException("Could not parse {} to float type".format(total_cost))
    return Receipt("Shop Name", total_cost, [])
    # raise NotImplementedError("TODO: Implement only_sum parsing strategy")