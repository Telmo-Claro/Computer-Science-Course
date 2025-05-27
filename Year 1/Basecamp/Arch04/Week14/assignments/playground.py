hashmap_key_value = {}
encoded_values = []
decoded_values = []


# a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$
def set_dict_key(key: str) -> None:
    for index in range(0, len(key), 2):
        hashmap_key_value[key[index]] = key[index + 1]
    return


def encode_function(data: str) -> str:
    while True:
        key = input(r"Key: ")
        if len(key) % 2 != 0:
            print("Invalid hashvalue input")
        else:
            set_dict_key(key)
            break
    set_dict_key(key)
    encoded_message = r""
    for letter in data:
        if letter in hashmap_key_value:
            letterInDict = True
        else:
            letterInDict = False
        if letterInDict is True:
            for key, value in hashmap_key_value.items():
                if key == letter:
                    encoded_message += value
                    break
        else:
            encoded_message += letter
    encoded_values.append(encoded_message)
    return encoded_message


def encode_string(data: str, hofunction) -> str:
    return hofunction(data)


def decode_function(data: str) -> str:
    while True:
        key = input(r"Key: ")
        if len(key) % 2 != 0:
            print("Invalid hashvalue input")
        else:
            set_dict_key(key)
            break
    set_dict_key(key)
    decoded_message = r""
    for letter in data:
        if letter in hashmap_key_value.values():
            letterInDict = True
        else:
            letterInDict = False
        if letterInDict is True:
            for key, value in hashmap_key_value.items():
                if value == letter:
                    decoded_message += key
                    break
        else:
            decoded_message += letter
    decoded_values.append(decoded_message)
    return decoded_message


def decode_string(data: str, hofunction) -> str:
    return hofunction(data)


def encode_list_function(data: list) -> list:
    encoded_list = list(map(encode_string(data, encode_function), data))
    return encoded_list


def encode_list(data: list, hofunction) -> list:
    return hofunction(data)


def decode_list_function(data: list) -> list:
    decoded_list = list(map(decode_string, data))
    return decoded_list


def decode_list(data: list, hofunction) -> list:
    return hofunction(data)


def validate_values_function(encoded: str, decoded: str) -> bool:
    encoded_to_decoded = decode_string(encoded)
    decoded_to_encoded = encode_string(decoded)
    if encoded_to_decoded == decoded and decoded_to_encoded == encoded:
        return True
    else:
        return False


def validate_values(encoded: str, decoded: str, hofunction) -> bool:
    return hofunction(encoded, decoded)


def print_all_values():
    for item in encoded_values:
        print(item)
    for item in decoded_values:
        print(item)


# Create a unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
def main():
    while True:
        user = input(
            """
[E] Encode value to hashed value
[D] Decode hashed value to normal value
[P] Print all encoded/decoded values
[V] Validate 2 values against eachother
[Q] Quit program
Input:
"""
        ).upper()
        if user == "E":
            message = input("Decoded message:\n > ")
            if "," in message:
                message = message.split(",")
                print(encode_list(message, encode_list_function))
            else:
                print(encode_string(message,encode_function))
        elif user == "D":
            message = input("Coded message: ")
            if "," in message:
                message = message.split(",")
                print(decode_list(message, decode_list_function))
            else:
                print(decode_string(message, decode_function))
        elif user == "P":
            print_all_values()
        elif user == "V":
            encoded = input("Encoded: ")
            decoded = input("Decoded: ")
            print(validate_values(encoded, decoded, validate_values_function))
        elif user == "Q":
            break
        else:
            print("INCORRECT INPUT")


if __name__ == "__main__":
    main()
