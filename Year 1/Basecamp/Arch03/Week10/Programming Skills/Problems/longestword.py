def show_last_ten(file):
    list_of_words = []
    list_of_longest_words = []
    try:
        with open(file, "r") as file:
            lines = file.readlines()
            for line in lines:
                words = line.split()
                for word in words:
                    list_of_words.append(word)
            longest_words = sorted(list_of_words, key=len, reverse=True)
            max_length = len(longest_words[0])
            # List comprehension, makes list out of words of max length
            list_of_longest_words = [word for word in longest_words if len(word) == max_length]
            print(f"Length of longest word is [{len(list_of_longest_words[0])}] chars")
            print("There are all the words of that length:")
            print(", ".join(list_of_longest_words))
    except FileNotFoundError:
        print("File not found")
    print("\n".join(list_of_longest_words))


if __name__ == "__main__":
    show_last_ten(input("Enter the file name: "))
