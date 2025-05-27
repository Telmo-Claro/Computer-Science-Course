#Get input
year = int(input("Year:"))

#Math

if year % 400 == 0:
    print("Leap Year")
else:
    if year % 100 == 0:
        print ("Not a leap year")
    else:
        if year % 4 == 0:
            print ("Leap year")
        else:
            print("Not a leap year")