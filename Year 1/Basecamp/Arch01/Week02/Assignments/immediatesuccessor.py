# Get input from user
dateEntered = input("Input Date: ").strip().split("-")

# Check if lengths of year, month, and day are correct
if len(dateEntered[0]) != 4 or len(dateEntered[1]) != 2 or len(dateEntered[2]) != 2:
    print("Input format ERROR. Correct Format: YYYY-MM-DD")
else:
    # Converts every item into integers
    year = int(dateEntered[0])
    month = int(dateEntered[1])
    day = int(dateEntered[2])

    # Checks if december is 12 and day is 31 so it changes the year goes to 1st of january
    if month == 12 and day == 31:
        year += 1
        month = 1
        day = 1
    else:
        # Just adds a day
        day += 1

        # Handle the 30 or the 31
        if month in [1, 3, 5, 7, 8, 10]:
            if day == 32:
                month += 1
                day = 1
        elif month in [4, 6, 9, 11]:
            if day == 31:
                month += 1
                day = 1
        elif month == 2:
            if day == 29:  # February always has 28 days
                month += 1
                day = 1

    # Output next date
    print(f"Next date: {year}-{month:02d}-{day:02d}")

# d indicates that the variable being formatted is an integer (specifically a decimal integer).
# 02 indicates that the integer should be formatted with at least 2 digits.
# If the integer has fewer than 2 digits, leading zeros are added to pad it to a width of 2 characters. (Yes chat GPT, but I understand :D)