import random


def get_word():
    file_to_read = input(r"Enter the name of the file to read: ")
    empty_list = []
    try:
        with open(file_to_read, "r") as file_to_read:
            list_words = file_to_read.readlines()
            for line in list_words:
                empty_list.append(line.removesuffix("\n"))
            word_one = random.choice(empty_list)
            word_two = random.choice(empty_list)
            final_word = word_one + word_two
            print(final_word)
            if 8 < len(final_word) < 10:
                print(final_word)
    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    get_word()
