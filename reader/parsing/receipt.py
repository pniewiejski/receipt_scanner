"""
Contains the definition of the Receipt class
"""
import json
from datetime import datetime
# from item import Item

class Receipt():
    """
    Instances of the Receipt class are structures for holding data retrieved from images of receipts.
    """
    def __init__(self, shop: str, total_cost: float, items: list, date: str=None):
        self.shop = shop
        self.totalCost = total_cost
        self.items = items
        if date is None: 
            self.date = str(datetime.now())
        elif isinstance(date, str): 
            self.date = datetime.strptime(date, )
        else: 
            raise TypeError("date cannot be of type: {}".format(type(date)))
    
    def to_json(self) -> str:
        """
        Serialize to JSON. Returns a str
        """
        return json.dumps(repr(self.__dict__))

# if __name__ == "__main__":
#     receipt = Receipt("Żabka", 20, [Item("NIC NACS XXL", 10, 2)])
#     print(receipt.to_json())