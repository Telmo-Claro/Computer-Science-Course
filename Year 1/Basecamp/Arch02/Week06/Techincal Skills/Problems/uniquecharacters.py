def unique_chars_dict(user):
    empty_dictionary = {}
    for char in user:
        if char not in empty_dictionary:
            empty_dictionary[char] = 1
    return len(empty_dictionary)


def unique_chars_set(user):
    ser_set = set(user)
    return len(ser_set)


if __name__ == "__main__":
    print(unique_chars_dict(input("")))
