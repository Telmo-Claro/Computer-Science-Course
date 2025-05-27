import random


#  #Operators
#  x = 7
#  x == 5
#  x == 7
#  x > 5
#  x < 10
#  5 < x < 10

#  vowels = "aeiou"
#  letter = "o"
#  letter in vowels
#  if letter in vowels:
#      print(letter, "is a vowel")

#  #book exercise
#  secret = 5
#  guess = 3
#  if guess < secret:
#      print("too low")
#  elif guess > secret:
#      print("too high")
#  else:
#      print("just right")

#  #book exercise
#  small = True
#  green = False
#  pea = small, green
#  watermelon = green

#  cherry = small
#  if cherry == cherry == watermelon:
#      print("Cherry is small and green!")
#  else:
#      print("Cherry is small but not green!")
#  a = True
#  b = False
#  print(a == b,
#        a != b,
#        a > b,
#        a < b,
#        a >= b,
#        a <= b)

#  cryptoList = ["Yeti", "Bigfoot", "Loch Ness Monster"]
#  cryptoString = ",".join(cryptoList)

#  #Book chapter 5 exercises
#  song = """When an eel grabs your arm,
#  And it causes great harm,
#  That's - a moray!"""

#  letterM = "m"
#  song.find(letterM)
#  song.replace(letterM, "M")

#  #5.2
#  questions = [
#  "We don't serve strings around here. Are you a string?",
#  "What is said on Father's Day in the forest?",
#  "What makes the sound 'Sis! Boom! Bah!'?"]

#  answers = [
#  "An exploding sheep.",
#  "No, I'm a frayed knot.",
#  "'Pop!' goes the weasel."
#  ]

#  q1 = (
#      f"Q: {questions[0]}"
#      + "\nA: "
#      + answers[1]
#      + "\nQ: "
#      + questions[1]
#      + "\nA: "
#      + answers[2]
#      + "\nQ: "
#      + questions[2]
#      + "\nA: "
#      + answers[0]
#  )

#  print(q1)

#  #Exercises github
#  food = str(input("Feed me a text: "))
#  print(len(food))
#  food = f"k{food[1:]}"

#  variableOne = "this is text"
#  variableOne = variableOne.replace(" ", "")

#  chicken = str(input("Input:").swapcase())

#  dog = str(input("Woof: "))
#  dog = dog.replace("e", "")

#  cat = str(input("Mew: "))
#  catLetter = "i"
#  cat = cat.count(catLetter)

#  catNdog = f"{dog} {cat}"

#  #Chapter 6 - Loops

# for count in range(1, 6):
#     print(count)
# while True:
#     stuff = input("String to capitalize [type q to quit]: ")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())

# while True:
#     value = input("Integer, please [q to quit]: ")
#     if value == "q": #quit
#         break
#     number = int(value)
#     if number % 2 == 0: #even number
#         continue
#     print(number, "squared is", number**2)

# numbers = [1, 3, 5,]
# position = 0
# while position < len(numbers):
#     number = numbers[position]
#     if number % 2 == 0:
#         print ("Found even number", number)
#         break
#     position += 1
# else: #break not called
#     print("No even number found")

# word = "thud"
# offset = 0
# for letter in word:
#     if letter == "x":
#         print("Eek! An ""x!")
#         break
#     print(letter)
# else:
#     print ("No x in there.")

# #exercises from book

# for x in range(3, -1, -1):
#     print(x)

# guessMe = 7
# number = 1

# while number <= guessMe:
#     print("Too low")
#     if number == guessMe:
#         print("Found it!")
#         break
#     if number >= guessMe:
#         print("Oops!")
#         break
#     number += 1

# guess_me = 5

# for number in range(10):
#     if number <= guess_me:
#         print("too low")
#     if number == guess_me:
#         print("Found it!")
#         break
#     if number >= guess_me:
#         print("Oops!")

# github loops exercises

# a = 0
# while a <= 41:
#     a += 1
#     print(a)

# i = 0
# while i < 100:
#    i = i + 2
#    print(i - 1)

# x = 11
# while x > -10:
#     x = x - 1
#     print(x)

# word = input("Test: ")
# b = 0
# while b < len(word):
#     if word[b] == "e" or word[b] == "a":
#         print(word[b])
#     b += 1

# i = -4
# end = -33
# while i > end:
#    i = i - 4
#    print(i * 2)

# i = -4
# end = -33
# while i > end:
#    print(i * 2)
#    i = i -4

# while True:
#     number = input("Enter a number [Enter Q to stop]: ")
#     if number == "q":
#         break
#     print(number)

# word = "thud"
# for letter in word:
#     print(letter)

# for i in range(1, 100, 2):
#     print(i)

# text = input("text: ")
# for i in text:
#     print(i)

# for i in range(3):
#     for j in range(2):
#         for x in range(5):
#             print(i, j, x)

# n = 4
# s = ""

# for i in range(n):
#     for j in range(i +1):
#         s += "* "
#     s += "\n"
# print(s)


# row = 1
# s = ""

# while row <= 4:
#     column = 1
#     while column <= row:
#         s +="* "
#         column += 1
#     s += "\n"
# print(s)

# Upside down triangle

# n = 4
# s = ""

# for row in range(n):
#     for space in range(n - row):
#         s += " "
#     for column in range(row+1):
#         s += "#"
#     s += "\n"

# print(s)

# map = [
# "[J][ ][E][ ][ ][Q][ ][F][ ][X]\n"
# "[ ]                        [ ]\n"
# "[R]                        [C]\n"
# "[ ]                        [ ]\n"
# "[Q]                        [ ]\n"
# "[ ]                        [Q]\n"
# "[ ]                        [ ]\n"
# "[C]                        [R]\n"
# "[ ]                        [ ]\n"
# "[X][ ][F][ ][Q][ ][ ][E][ ][S]"]
# print(map)

# Functions


# def make_a_sound():
#     print("quack")

# make_a_sound()


# def agree():
#     return True
# if agree():
#     print("Splendid!")
# else:
#     print("That was unexpected")


# def commentary(color):
#     if color == "red":
#         return "It's a tomato."
#     elif color == "green":
#         return "It's a green pepper."
#     elif color == "bee purple":
#         return "I don't know what it is, but only bees can see it."
#     else:
#         return "I've never heard of the color " + color + "."

# comment = commentary("blue")

# print(comment)


# def greet():
#     print("Hello")

# greet()


# def text(word):
#     print(f"{word}")

# text("Telmo")


# def meth(a, b):
#     print(a + b)
# meth(32, 21)


# def int1(a):
#     return a // 2

# def int2(b):
#     return b * 10

# print(int1(2) + int2(7))


# def hello():
#     print("Hello")
#     bye()

# def bye():
#     print("Bye")

# hello()


# Tuples

# numbers = (1, 2)
# letters = ("gaming", "space")
# print(numbers + letters)

# numbers = (1, 2, 3)
# for i in numbers:
#     i *= 2
#     print(i)

# def tuples():
#     x = ("Big", "Booty", "Latina")
#     a, b, c = x
#     print(a, b, c)
# tuples()

# Lists

# scores = [1,2,3,4,5,6,7,8,9,10]
# print(scores[0:2], scores[8:10])

# numbers = input("List of integers: ").split()

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# print(numbers)
# print(numbers[-1])

# numbers.reverse()
# print(numbers)
# numbers.reverse()

# for x in numbers:
#     if not x % 5:
#         print("Yes")
#         break
#     else:
#         print("No")

# count = 0
# for y in numbers:
#     if not y % 5:
#         count += 1
#     else:
#         continue
# print(count)

# nocount = 0
# for p in numbers:
#     if p % 5:
#         nocount += 1
#     else:
#         continue
# print(nocount)

# list = []
# for x in range(1, 20):
#     random_number = random.randrange(1,101)
#     list.append(random_number)
# print(list)

# def average(list):
#     return sum(list) / len(list)

# print(round(average(list)))

# list.sort()
# def largest(list):
#     return max(list)
# def smallest(list):
#     return min(list)

# print(largest(list))
# print(smallest(list))

# list.sort()
# print(list)
# second_smallest = list[1]
# second_largest = list[-2]
# print(second_largest)
# print(second_smallest)

# even_count = 0
# for q in list:
#     if q % 2 == 0:
#         even_count += 1
#     else:
#         continue
# print(even_count)

# list=[8,9,10]
# print(list)
# list.insert(1, 17)
# print(list)
# list.append(4)
# list.append(5)z
# list.append(6)
# print(list)
# list.pop(0)
# print(list)
# list.sort()
# print(list)
# copy = list.copy()
# list = list + copy
# print(list)
# list.insert(3, 25)
# print(list)

# count = 1
# list = []
# for x in range(0, 50):
#     list.append(count)
#     count += 1
# print(list)

# count = 0
# list = []
# for x in range(1, 51):
#     square = count * count
#     list.append(square)
#     count += 1
# print(list)

# list = [chr(i) for i in range(65, 90)]
# empty = []
# print(list)
# count = 1

# for i in list:
#     replace = i * count
#     count += 1
#     empty.append(replace)
# print(empty)

# L = [3,1,4]
# M = [1,5,9]
# N = []

# for L, M in zip(L, M):
#     new = L + M
#     N.append(new)
# print(N)

# dictionary = {"FirstName": "Larry", "LastName": "Page"}
# print(dictionary.get("LastName"))

# car = {"brand":"Ford",
#        "model":"Mustang",
#        "year":1964}
# print(car.values())
# print(car.keys())
# print(len(car))

# car["color"] = "red"
# car.pop("year")

# print(car.keys())
# print(car.values())

# def random_numbers():
#     return (random.randint(1, 100), random.randint(1, 100))

# for item in car:
#     car[item] = random_numbers()

# print(car)

# e2f = {
#     "dog": "chien",
#     "cat": "chat",
#     "walrus": "morse",
# }


# print(e2f["walrus"])

# print(e2f.items())
# f2e = {value: key for key, value in e2f.items()}
# print(f2e)
# print(f2e["chien"])
# print(e2f.keys())

# life = {
#     "animals": {
#         "cats": {("Henri", "Grumpy", "Lucy")},
#         "octopi": {},
#         "emus": {},
#     },
#     "plants":{

#     },
#     "other":{

#     },
# }

# print(life.keys())
# print(life["animals"].keys())
# print(life["animals"]["cats"])

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even = list(filter(lambda x: x % 2 == 0, numbers))
# odd = list(filter(lambda x: x % 2 != 0, numbers))

# even = lambda x: x % 2 == 0
# print(even(4))
# print(even(13))

"""Complete the function that checks if a given list is sorted or not, 
use at least one lambda within the function."""

# def am_i_sorted(numberlist):
#     #write the code
#     for i in range(len(numberlist) - 1):
#         if(lambda x,y : x > y)(numberlist[i],numberlist[i + 1]):
#             return False
#     return True
#     ...


# result = am_i_sorted([1,2,5,6,8,17])
# print(result) #True
# result = am_i_sorted([1,2,99,6,8,17])
# print(result) #False


# x = lambda a,b:(a,b)
# print(x(1,2))

# Complete the function that checks if the items in a given list
# are True for the given lambda.
# Return a list containing all True values.

# def check_with_lambda(lam, l):
#     #write the code
#     x = filter (lam, l)
#     x = list(x)
#     return x
#     ...

# x = lambda a : a < 10
# y = [1,6,19,22,7]
# print(check_with_lambda(x, y)) #[1,6,7]
# x = lambda a : a[1] == 'b'
# y = ["abc", "bcd", "ube", "cur"]
# print(check_with_lambda(x, y)) #["abc","ube"]

# list1 = [1,2,5,4,3]
# list1.sort(reverse=True)
# print(list1)

# number_tuples = [(10, 20, 30), (15, 25, 35), (5, 15, 25)]
# for x in number_tuples:
#     print(x[-1])
# print(number_tuples)

"""Complete the function that returns a 
list containing all the values from all tuples in the given list."""
# def create_list_from_tuples(a):
#     #write the code
#     empty_list = []
#     for x in a:
#         for i in x:
#             empty_list.append(i)
#     return empty_list

# l = [(1,5,4),(1,2),(8,5,19,0)]
# print(create_list_from_tuples(l))
# # [1,5,4,1,2,8,5,19,0]


# def create_list_from_tuples(a):
#     # write the code
#     empty_list = []
#     for x in a:
#         m = sorted(x)
#         empty_list.append(m)
#     return empty_list


# l = [(1, 5, 4), (1, 2), (8, 5, 19, 0)]
# print(create_list_from_tuples(l))
# # [1,5,4,1,2,8,5,19,0]

# result_list = []
# for i in range(1, 10, 2):
#     result_list.append((i, i + 1))
# print(result_list)

# the_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# filtered_list = list(filter(lambda x: x[0] % 2 == 0, the_list))
# print(filtered_list)

"Complete the function to merge two lists into one dictionary."

# def merge_lists_into_dictionary(l1, l2):
#     result = dict(map(lambda i,j : (i,j), keys,values))
#     return result

# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# result = merge_lists_into_dictionary(keys, values)
# print(result) #{'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}

""". Given is a list of dictionaries. 
Sadly the values are the wrong way around. 
The first value should be at the last key, 
second value at the second from last key, and so on. 
Create a function that switches these values for each list you could give it. """


# def switch_the_values(l):
#     # Write the code
#     values_list = []
#     keys_list = []
#     list_positive = []

#     for i in l:
#         keys_list.append(list(i.keys())[0])
#         values_list.append(list(i.values())[0])

#     values_list = list(reversed(values_list))

#     dictionary_maker = dict(map(lambda i, j: (i, j), keys_list, values_list))
#     list_positive.append(dictionary_maker)
#     return list_positive


# x = [{"Math": 81}, {"Physics": 83}, {"Chemistry": 87}, {"English": 42}]
# print(switch_the_values(x))
# # [{'Math':42}, {'Physics':87}, {'Chemistry':83}, {'English': 81}]
# x = [{"a": "b"}, {"c": "d"}]
# print(switch_the_values(x))
# # [{'a':'d'}, {'c':'b'}]

"""Given is a dictionary with tuples. Complete to code to add all keys, 
at which the second Tuple value is Pass, to a list and return that list """


# def create_pass_list(l):
#     # Write the code
#     list_positive = []
#     list_negative = []
#     new_dict = {"Pass": "", "Fail": ""}
#     for i in l.items():
#         for x in i:
#             if x[-1] == "Pass":
#                 list_positive.append(i[0])
#             elif x[1] == "Fail":
#                 list_negative.append(i[0])

#     new_dict["Pass"] = list_positive
#     new_dict["Fail"] = list_negative

#     return new_dict


# x = {
#     "Math": (81, "Pass"),
#     "Physics": (50, "Fail"),
#     "Chemistry": (90, "Pass"),
#     "English": (42, "Fail"),
# }


# ultimate_dictionary = create_pass_list(x)
# print(ultimate_dictionary)
# ["Math", "Chemistry"]

"""
Write a function that takes the dictionary from the previous exercise and 
turns each value into his own key:value pair. Sort the dictionary by the key. 
The result should be: 
{'Chemistry': 'Pass', 'English': 'Fail', 'Math': 'Pass', 'Physics': 'Fail'}; 
"""


# def ordered_dictionary(d):
#     pass_list = []
#     fail_list = []
#     new_keys = []
#     new_values = []
#     new_dictionary = {}
#     for item in d.items():
#         if "Pass" in item:
#             print(item)
#             pass_list.append(item[-1])
#             pass_list = item[-1]
#         else:
#             fail_list = item[-1]
#     for item in pass_list:
#         new_keys.append(item)
#         new_values.append("Pass")
#     for item in fail_list:
#         new_keys.append(item)
#         new_values.append("Fail")
#     new_dictionary = dict(sorted(zip(new_keys, new_values)))
#     return new_dictionary


# print(ordered_dictionary(ultimate_dictionary))
