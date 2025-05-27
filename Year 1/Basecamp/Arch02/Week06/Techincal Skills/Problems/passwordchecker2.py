allowed = {
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "*", "@", "!", "?"
}


if __name__ == "__main__":
    count = 3
    while count > 0:
        password = input("Password: ")
        password_set = set(password)
        if not (8 <= len(password) <= 20):
            print("Password is invalid")
            count -= 1
            print(f"You have {count} more tries.")
            continue
        if password_set.issubset(allowed):
            print("Password is valid")
            break
        count -= 1
        print(f"You have {count} more tries.")