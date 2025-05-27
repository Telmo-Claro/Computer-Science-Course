#Get input of the cost
cost = float(input("Cost:"))

#Calculate tip, tax and total
tip = cost * 0.15
tax = cost * 0.21
total = tip + tax + cost
round(total, 3)

#Show output
print(f"Tax: {tax}, Tip: {tip}, Total: {total}")
