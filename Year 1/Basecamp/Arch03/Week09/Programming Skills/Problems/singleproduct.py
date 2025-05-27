class Product:
    # Product name, amount of that product in stock, and price per unit
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
        """
        Under 10 no discount.
        Between 10 and 99 give 10% discount.
        100 or more give 20% discount.
        """
        if quantity < 10:
            self.total_price = self.price * quantity
        elif quantity < 99:
            self.total_price = self.price * quantity * 0.9
        else:
            self.total_price = self.price * quantity * 0.8
        return self.total_price

    def make_purchase(self, quantity):
        self.amount = self.amount - quantity
        return self.amount
