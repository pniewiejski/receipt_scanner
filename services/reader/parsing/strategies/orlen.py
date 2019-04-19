"""
Parse receipt from Orlen 
"""
import re
from parsing.receipt import Receipt 
from parsing.item import Item
from parsing.strategies import comma_to_dot
from parsing.parsing_error import ParsingException

def orlen(text: str) -> Receipt:
    """
    Extract: 
        * sum
        * fuel type

    Errors:
        * `ParsingException` is raised on fail
    """
    shop_name = re.search(r"(Polski Koncern Naftowy ORLEN S\.A\.)", text, re.IGNORECASE)
    if shop_name is not None: 
        shop_name = shop_name.group(1)
    else: 
        shop_name = "Shop name"
    
    fuel = re.search(r"([A-Z][A-Z\s]*[A-Z]*)\s*CN27.*\s([\d\.,]+)\*([\d\.,]*)", text)
    if fuel is not None:
        try:
            fuel_type = fuel.group(1).strip()
            fuel_amount = float(comma_to_dot(fuel.group(2)))
            fuel_price = float(comma_to_dot(fuel.group(3)))
        except:
            raise ParsingException("Could not parse fuel info to float type.")
    else: 
        raise ParsingException("Parsing could not yield anthing interesting. No match error.")

    parsed_cost = re.search(r"SU[MN][ĄA]\s*[-:;]{0,1}\s*P?L?N?\s*(\d+[\.,]\d\d)", text, re.IGNORECASE)
    if parsed_cost is not None:
        parsed_cost = parsed_cost.group(1)
        parsed_cost = comma_to_dot(parsed_cost)
        try:
            total_cost = float(parsed_cost)
        except:
            raise ParsingException("Could not parse {} to float type".format(total_cost))
    else: 
        raise ParsingException("Parsing could not yield anthing interesting. No match error.")
    return Receipt(shop_name, 
                    total_cost, 
                    [Item(fuel_type, fuel_price, fuel_amount)]
                )
    

