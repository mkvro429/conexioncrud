from typing import Any


class Product:
    def __call__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity 
    def toDBcollection(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }
    