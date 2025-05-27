dict_key_value = {}
encoded_values = []
decoded_values = []


def set_dict_key(key: str) -> None:
    for index in range(0, len(key), 2):
        dict_key_value[key[index]] = key[index + 1]
    return


def encode_string(data: str, key: str = None) -> str:
    encoded_message = r""
    for letter in data:
        if letter in dict_key_value:
            letterInDict = True
        else:
            letterInDict = False
        if letterInDict is True:
            for key, value in dict_key_value.items():
                if key == letter:
                    encoded_message += value
                    break
        else:
            encoded_message += letter
    encoded_values.append(encoded_message)
    return encoded_message


def test_encode_string():
    set_dict_key("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")
    # check if given the hashmap string, the correct output is given
    assert "**9 (?##*(;* :0;=?!5;" == encode_string("EEN CORRECTE UITKOMST")
    # check if case insesitive input is handle correctly
    assert "*en (orrecte :itkomst" == encode_string("Een Correcte Uitkomst")


def decode_string(data: str, key: str = None) -> str:
    decoded_message = r""
    for letter in data:
        if letter in dict_key_value.values():
            letterInDict = True
        else:
            letterInDict = False
        if letterInDict is True:
            for key, value in dict_key_value.items():
                if value == letter:
                    decoded_message += key
                    break
        else:
            decoded_message += letter
    decoded_values.append(decoded_message)
    return decoded_message


lambda x: print()


def encode_list(data: list, key: str = None) -> list:
    encoded_list = list(map(encode_string, data))
    return encoded_list


def decode_list(data: list, key: str = None) -> list:
    decoded_list = list(map(decode_string, data))
    return decoded_list


def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    encoded_to_decoded = decode_string(encoded)
    decoded_to_encoded = encode_string(decoded)
    if encoded_to_decoded == decoded and decoded_to_encoded == encoded:
        return True
    else:
        return False


def print_all_values():
    for item in encoded_values:
        print(item)
    for item in decoded_values:
        print(item)


def main():
    while True:
        key = input(r"Key: ")
        if len(key) % 2 != 0:
            print("Invalid hashvalue input")
            key_selected = False
            break
        else:
            set_dict_key(key)
            key_selected = True
            break
    while key_selected:
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
            message = input("Decoded Message: ")
            if "," in message:
                message = message.split(",")
                print(encode_list(message))
            else:
                print(encode_string(message))
        elif user == "D":
            message = input("Coded message: ")
            if "," in message:
                message = message.split(",")
                print(decode_list(message))
            else:
                print(decode_string(message))
        elif user == "P":
            print_all_values()
        elif user == "V":
            encoded = input("Encoded: ")
            decoded = input("Decoded: ")
            print(validate_values(encoded, decoded))
        elif user == "Q":
            break
        else:
            print("INCORRECT INPUT")


if __name__ == "__main__":
    main()