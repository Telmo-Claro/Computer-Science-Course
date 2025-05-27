#Get input from user in the form of an integer
year = int(input("Years:"))

#Calculate month and day
month = 12 * year
day = 365 * year

#Show output
print (f"Months: {month}, Days: {day}")