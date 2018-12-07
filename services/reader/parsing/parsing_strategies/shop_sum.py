"""
Find SUM and SHOP NAME
"""
import re
from parsing.receipt import Receipt # relative import - life is full of zasadzkas
from parsing.parsing_strategies import comma_to_dot
from parsing.errors.parsing_error import ParsingException

def shop_sum(text: str) -> Receipt:
    """
    Extract only the SUM value

    Errors
    ------
    `ParsingException` is raised on fail
    """
    #search_for = re.compile(r"SUMA:{0,1}\s*(\d[\.,]\d\d)", re.IGNORECASE)
    shop_name = extract_shop_name(text)
    if shop_name == None:
        shop_name = "Shop Name"
    parsed = re.search(r"SU[MN][ĄA][:;]{0,1}\s*P?L?N?\s*(\d+[\.,]\d\d)", text, re.IGNORECASE)
    if parsed is not None:
        parsed = parsed.group(1)
        parsed = comma_to_dot(parsed)
        try:
            total_cost = float(parsed)
        except:
            raise ParsingException("Could not parse {} to float type".format(total_cost))
        return Receipt(shop_name, total_cost, [])
    else: 
        raise ParsingException("Parsing could not yield anthing interesting. No match error.")

def extract_shop_name(text):
    parsed = re.search(r"[\s\S]*?(?=[\r\n])", text, re.IGNORECASE)
    return parsed.group(0)
