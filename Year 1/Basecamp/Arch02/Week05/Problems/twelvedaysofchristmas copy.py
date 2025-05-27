# "[Verse 1]
# On the 1st day of Christmas, my true love sent to me A partridge in a pear tree

# [Verse 2]
# On the 2nd day of Christmas, my true love sent to me Two turtledoves And A partridge in a pear tree

# [Verse 3]
# On the 3rd day of Christmas, my true love sent to me Three French hens, Two turtledoves And A partridge in a pear tree

# [Verse 4]
# On the 4th day of Christmas, my true love sent to me Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree

# [Verse 5]
# On the 5th day of Christmas, my true love sent to me Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree

# [Verse 6]
# On the 6th day of Christmas, my true love sent to me Six geese a-laying, Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree

# [Verse 7]
# On the 7th day of Christmas, my true love sent to me Seven swans a-swimming, Six geese a-laying, Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree

# [Verse 8]
# On the 8th day of Christmas, my true love sent to me Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree

# [Verse 9]
# On the 9th day of Christmas, my true love sent to me Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree

# [Verse 10]
# On the 10th day of Christmas, my true love sent to me Ten lords a-leaping, Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings (five golden rings),
# Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree

# [Verse 11]
# On the 11th day of Christmas, my true love sent to me Eleven pipers piping, Ten lords a-leaping, Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree

# [Verse 12]
# On the 12th day of Christmas, my true love sent to me Twelve drummers drumming, Eleven pipers piping, Ten lords a-leaping, Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree"


def next_verse(vers_number: int) -> str:
    if vers_number == 1:
        return ("On the 1st day of Christmas, my true love sent to me A partridge in a pear tree")
    elif vers_number == 2:
        return ("On the 2nd day of Christmas, my true love sent to me Two turtledoves And A partridge in a pear tree")
    elif vers_number == 3:
        return ("On the 3rd day of Christmas, my true love sent to me Three French hens, Two turtledoves And A partridge in a pear tree")
    elif vers_number == 4:
        return ("On the 4th day of Christmas, my true love sent to me Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree")
    elif vers_number == 5:
        return  ("On the 5th day of Christmas, my true love sent to me Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree")
    elif vers_number == 6:
        return ("On the 6th day of Christmas, my true love sent to me Six geese a-laying, Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree")
    elif vers_number == 7:
        return ("On the 7th day of Christmas, my true love sent to me Seven swans a-swimming, Six geese a-laying, Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree")
    elif vers_number == 8:
        return ("On the 8th day of Christmas, my true love sent to me Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree")
    elif vers_number == 9:
        return ("On the 9th day of Christmas, my true love sent to me Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree")
    elif vers_number == 10:
        return ("On the 10th day of Christmas, my true love sent to me Ten lords a-leaping, Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree")
    elif vers_number == 11:
        return ("On the 11th day of Christmas,my true love sent to me Eleven pipers piping, Ten lords a-leaping, Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree")
    elif vers_number == 12:
        return ("On the 12th day of Christmas, my true love sent to me Twelve drummers drumming, Eleven pipers piping, Ten lords a-leaping, Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings (five golden rings), Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree")


if __name__ == "__main__":
    for verse in range(1, 13):
        print(next_verse(verse))
