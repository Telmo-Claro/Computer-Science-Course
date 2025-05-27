#Get input in the form of a string as a, b, c.
stringInput = input("Sides as: a=1, b=2, c=3: ")
sides = stringInput.split(",")

#Checks if the length (len) of the sides is 3
if len(sides) != 3:
    print("Try again.")
#Sets a letter to each length
else:
    a = int(sides[0].split("=")[1].strip())
    b = int(sides[1].split("=")[1].strip())
    c = int(sides[2].split("=")[1].strip())

#Checks the type of triangle.
if a == b == c:
    print("Equilateral triangle")
elif a == b or a == c or b == c:
    print ("Isosceles triangle")
else: print ("Scalene triangle")