import re

#Using regular expressions, tell which licenses are valid
valid = [r"[A-Z]{2}-\d{2}-\d{2}", 
         r"\d{2}-\d{2}-[A-Z]{2}", 
         r"\d{2}-[A-Z]{2}-\d{2},",
         r"[A-Z]{2}-\d{2}-[A-Z]{2}",
         r"[A-Z]{2}-[A-Z]{2}-\d{2}",
         r"\d{2}-[A-Z]{2}-[A-Z]{2}",
         r"\d{2}-[A-Z]{3}-\d{1}",
         r"\d{1}-[A-Z]{3}-\d{2}",
         r"[A-Z]{2}-\d{3}-[A-Z]{1}",
         r"[A-Z]{1}-\d{3}-[A-Z]{2}",
         r"[A-Z]{3}-\d{2}-[A-Z]{1}",
         r"\d{1}-[A-Z]{2}-\d{3}"]

#Get input from user.
license = input("License: ")

#Uses a function from the re library to see if both x and valid match.
for x in valid:
    if re.match(x, license):
        print("Valid")
        exit(0)
    else:
        print("Invalid")