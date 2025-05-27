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

# def numbers(*args):
#     print(sum(args))
# numbers(1,2,3)


# def count_passes(**kwargs):
#     count = 0
#     # Complete this function to count the number of passes
#     print(kwargs)
#     for value in kwargs.values():
#         if value == "Pass":
#             count += 1
#     return count

# result = count_passes(math="Fail", science="Fail", history="Pass", english="Pass")
# print(result)

# random_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# print(len(random_set))
# print(list(random_set)[-1])


# dic = {"first_name":"Peter",
#         "last_name":"File",}

# def argument(dictionary):
#     print(set(dictionary.values()))

# argument(dic)

# letters = {"x","y","q","z","u"}
# user = input("Letter: ").lower()
# if user in letters:
#     print("Yes")
# else:
#     print("No")


