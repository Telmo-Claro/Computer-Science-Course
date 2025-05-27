position = input("Position as A1: ").strip().upper()

#Separate the string and int
letter = position[0]
num = int(position[1])

#if letter is A, change A to 0
if letter in ["A", "C", "E", "G"]:
    letter = 0
if letter in ["B", "D", "F", "H"]:
    letter = 1
    
print(letter)

if letter + num in [1, 3, 5, 7]:
    letter = "Black"
else:
    letter = "White"

print(letter)