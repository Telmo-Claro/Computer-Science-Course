class Customer:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Name: {self.name}")


class Car:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.sold_to = None

    def sell(self, customer):
        self.sold = True
        if customer is not None:
            self.sold_to = customer
        return self.sold, self.sold_to

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color {self.color}")
        print(f"Price: {self.price}")
        if self.sold:
            print(f"Sold to: {self.sold_to.name}")
        else:
            print("Not sold yet")


class Motorcycle:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.sold_to = None

    def sell(self, customer):
        self.sold = True
        if customer is not None:
            self.sold_to = customer
        return self.sold, self.sold_to

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color {self.color}")
        print(f"Price: {self.price}")
        if self.sold:
            print(f"Sold to: {self.sold_to.name}")
        else:
            print("Not sold yet")


if __name__ == "__main__":
    customer = Customer("John Doe")
    car = Car("AUDI", "A3", "BLUE", 19.999)
    car.sell(customer)
    car.print()
