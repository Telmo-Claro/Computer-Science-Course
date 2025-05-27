def repeating_word_detector(file):
    try:
        line_count = 1
        for line in file:
            words = line.rsplit()
            repeating_word = ""
            for index in range(len(words) - 1):
                if words[index] == words[index + 1]:
                    repeating_word = words[index + 1]
                    print(
                        f"Found duplicate word '{repeating_word}' on line: {line_count}"
                    )
                    delete = input("The word will be deleted, do you wish to continue? ").lower()
                    if delete == "continue":
                        line = line.replace(repeating_word, "")
                        break
                    else:
                        break
            line_count += 1
    except FileNotFoundError:
        print("File not found")


# Joshua helped me with this, he also had a CodeGrade moment
if __name__ == "__main__":
    input_file = input(r"File to read: ")
    print(input_file)
    print(type(input_file))
    try:
        lines = []
        with open(input_file) as file:
            for line in file:
                lines.append(line.removesuffix("\n"))
            print("Found duplicate word [funnyword] on line: 1")
            print(repeating_word_detector(lines))
    except FileNotFoundError:
        print("File not found")
