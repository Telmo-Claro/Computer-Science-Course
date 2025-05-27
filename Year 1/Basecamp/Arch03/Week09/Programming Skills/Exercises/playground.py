# # Creating a class
# class Car:
#     def __init__(self, color, make, model):
#         self.color = color
#         self.make = make
#         self.model = model

#     def start_engine(self):
#         print(f"Start the {self.color} {self.make} {self.model} engine.")


# # Creating an instance
# my_car = Car("Red", "Toyota", "Yaris")
# your_car = Car("Black", "Ferrari", "Roma")

# print(my_car.start_engine())
# print(your_car.start_engine())


# class Rectangle:
#     def __init__(self, length, width):
#         self.lenght = length
#         self.width = width

#     def area(self):
#         area = self.lenght * self.width
#         return area

#     def perimeter(self):
#         perimeter = (self.lenght * 2) + (self.width * 2)
#         return perimeter


# rectangle_1 = Rectangle(4, 2)
# print(rectangle_1.area())
# print(rectangle_1.perimeter())


# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         self.balance -= amount

#     def get_balance(self):
#         return self.balance


# poor_dad = BankAccount(2000.0)
# poor_dad.deposit(1000)
# poor_dad.deposit(299)
# poor_dad.withdraw(5000)
# print(poor_dad.get_balance())


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __repr__(self) -> str:
#         return f"Title: {self.title} , Author: {self.author}"


# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []

#     def add_books(self, books):
#         self.books = books

#     def display_books(self):
#         print(f"Books in {self.name} Library:")
#         for book in self.books:
#             print(book)


# def main():
#     # Create Books
#     book1 = Book("Introducing Python", "Bill Lubanovic")
#     book2 = Book("The Python Workbook", "Ben Stephenson")
#     book3 = Book("Learn Python Programming", "Fabrizio Romano")
#     book4 = Book("Fleunt Python", "Luciano Ramalho")
#     # Create libraries
#     univ_lib = Library("University")
#     city_lib = Library("City")
#     # Add books to the libraries
#     univ_lib.add_books([book1, book4])
#     city_lib.add_books([book1, book3])
#     univ_lib.add_books([book1, book2])
#     city_lib.add_books([book3, book4])
#     # Display books in libraries
#     univ_lib.display_books()
#     city_lib.display_books()


# main()


class Car:
    sold = False

    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    def sell(sold):
        sold = True

    def show_car(self, sold):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color {self.color}")
        print(f"Price: {self.price}")
        if sold:
            print("Sold")
        else:
            print("Not sold yet")

if __name__ == "__main__":
    car_1 = Car("BMW", "X5", "Black", 34.899)
    print(car_1.show_car(sold=False))
