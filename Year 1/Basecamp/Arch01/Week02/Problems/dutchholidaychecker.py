#Get input in the form of a string as Month:, Day:
stringInput = input("Date as Month:1, Day:1 ")
date = stringInput.split(",")

#Check if the length of the date is 2
if len(date) != 2:
    print("Try again!")
else:
    month = int(date[0].split(":")[1].strip())
    day = int(date[1].split(":")[1].strip())
    
#Check the date
if month == 1 and day == 1:
    print("Nieuwjaarsdag")
elif month == 3 and day == 29:
    print("Goede vrijdag")
elif month == 4 and day == 27:
    print("Koninsdag")
elif month == 5 and day == 5:
    print("Bevrijdingsdag")
elif month == 12 and day == 25 or day == 26:
    print("Kerstmis")
else: print("No holiday found on given input")