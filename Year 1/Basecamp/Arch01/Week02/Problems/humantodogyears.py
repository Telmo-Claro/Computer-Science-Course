num = int(input("Human years: "))

if num < 0:
    print("Only positive numbers are allowed") 
else:
    if num == 1:
        age = 10.5
    elif num == 2:
        age = 21
    else:
        age = 21 + (num - 2) * 4
    print(f"Dog years: {age}")
