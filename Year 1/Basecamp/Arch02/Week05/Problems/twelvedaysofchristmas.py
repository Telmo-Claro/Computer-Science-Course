"""[Verse 1]
On the first day of Christmas, my true love sent to me
A partridge in a pear tree

[Verse 2]
On the second day of Christmas, my true love sent to me
Two turtle doves and
A partridge in a pear tree

[Verse 3]
On the third day of Christmas, my true love sent to me
Three french hens
Two turtle doves and
A partridge in a pear tree

[Verse 4]
On the fourth day of Christmas, my true love sent to me
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree

[Verse 5]
On the fifth day of Christmas, my true love sent to me
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree
You might also like
Did you know that there's a tunnel under Ocean Blvd
Lana Del Rey
Evil Ways
Drake
The Shoe Fits
Drake
[Verse 6]

On the sixth day of Christmas, my true love sent to me
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree

[Verse 7]
On the seventh day of Christmas, my true love sent to me
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree

[Verse 8]
On the eighth day of Christmas, my true love sent to me
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree

[Verse 9]
On the ninth day of Christmas, my true love sent to me
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree

[Verse 10]
On the tenth day of Christmas, my true love sent to me
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree

[Verse 11]
On the eleventh day of Christmas, my true love sent to me
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree

[Verse 12]
On the twelfth day of Christmas, my true love sent to me
Twelve drummers drumming
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree"""


def next_verse(vers_number: int) -> str:
    days_of_christmas = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
    ]
    list_gifts_in_order = [
        "A partridge in a pear tree",
        "Two turtle doves",
        "Three french hens",
        "Four calling birds",
        "Five golden rings (five golden rings)",
        "Six geese a-laying",
        "Seven swans a-swimming",
        "Eight maids a-milking",
        "Nine ladies dancing",
        "Ten lords a-leaping",
        "Eleven pipers piping",
        "Twelve drummers drumming",
    ]
    all_together = (
        f"On the {days_of_christmas[vers_number - 1]} day of Christmas, my true love sent me "
    )
    # Loop to get each gift after the all_together song with the day of christmas
    for index, gifts in enumerate(range(vers_number, 0, -1)):  # Goes from bottom to top of the list
        gift = list_gifts_in_order[gifts - 1].capitalize()  # Capitalize the first letter of each gift
        if index == 0:
            all_together += gift + ","
        else:
            all_together += gift
        if gifts != 1:
            all_together += " and ".capitalize()
    return all_together


if __name__ == "__main__":
    for verse in range(1, 13):
        print(next_verse(verse))
