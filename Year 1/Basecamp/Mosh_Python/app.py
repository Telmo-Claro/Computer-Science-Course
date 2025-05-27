# print("Sup G!")
# print("O----")
# print(" ||||")
# print("*" * 10)

"""
What is inside () is called an expression.
A string is a continuation of characters.
"""

# Next lesson - Data types and variables
price = 10
rating = 4.9

"""
Numbers without a decimal point are called integers
With decimal point numbers are called float
True or False are called booleans
"""

# Exercise from video
full_name = "John Smith"
age = 20
new_patient = True

"""
Concatenate means to combine strings (or any data type)
Next lesson - Get input, use input
"""

# name = input("What is your name? ")
# print("Hello " + name + "!")
# favorite_color = input("What is your favorite colour? ")
# print(f"{name} likes {favorite_color}")

"""
Type conversation
int()
float()
bool()
str()
"""
# birth_year = input("Birth year: ")
# age_today = 2024 - int(birth_year)
# print(age_today)

# weight_in_pounds = int(input("What is your weight in pounds? "))
# weight_in_kg = weight_in_pounds / 2.2046
# print(weight_in_kg, "kg")

"""
Strings
"""

# first = "John"
# last = "Smith"
# message = first + " [" + last + "] is a coder"
# msg = f"{first} [{last}] is a coder"
# print(msg)

course = "Python for Beginners"
len(course)  # Counts number of charachter with a function
course.upper()
"Python" in course  # Boolean expression, should return True. find() gives index

# Function: General use (len())
# Method: Specific use (.upper(), find(), replace(), title())

"""
Arithmetic Operations
"""
# / = 3.333, // = 3, % = remainder, ** exponent
x = 10
x -= 3  # Augmented

"""
Operator Precedence
"""
x = 10 + 3 * 2**2

# Parenthesis
# Exponentiation 2 ** 3
# Multiplication or division
# Addition or subtraction

"""
Math functions
"""
import math

# It's a module

math.floor(2.9)
x = 2.9
# print(round(x))
# print(abs(-2.9))

"""
If statements
"""

is_hot = False
is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

"""
Exercise
"""
# price = 1000000

# good_credit = True

# if good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: €{down_payment}")

"""
Logical Operators

if ... AND ...  --- both have to be True
if ... OR ...   --- only one has to be True
NOT (reverses boolean value)
"""

has_high_income = True
has_good_credit = True
has_criminal_record = False

# if has_high_income and not has_criminal_record: # not False = True, not True = False
#     print("Eligible for loan")

"""
Comparison Operators
> bigger than
< smaller than
== equals to
!= not equal to
"""

temperature = 30

# if temperature > 30: # This is a boolean expression, returns True or False
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

"""
Exercise
"""

name = "Stephan Salvatore"

# if len(name) < 3:
#     print("Name must be at least 3 charachters")
# elif len(name) > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good!")

# weight = float(input("Weight: "))
# unit = input("[L]bs or [K]g: ").upper()

# if unit == "L":
#     lbs_to_kg = weight * 0.45
#     print(f"You are {lbs_to_kg} kilograms.")
# else:
#     kg_to_lbs = weight * 2.2046
#     print(f"You are {kg_to_lbs} pounds.")

"""
While loops
"""

# i = 1
# while i <= 5:
#     print("X" * i)
#     i += 1
# print("Done")

# secret_number = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
#     else:
#         print("You failed!")

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     if command == "help":
#         print(f"start - to start the car")
#         print(f"stop - to stop the car")
#         print(f"quit to exit")
#     elif command == "start":
#         print(f"Car started...")
#     elif command == "stop":
#         print(f"Car stopped...")
#     else:
#         print("I don't understand that...")
