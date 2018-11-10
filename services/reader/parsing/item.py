"""
Contains the definition of the Item class
"""

class Item:
    """
    Instances of the Item class are structures for holding data about single product.
    """
    def __init__(self, name: str, price: float, quantity: float=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return repr(self.__dict__)
    