def censor_file(file_to_censor, words_to_censor, redacted_file):
    bad_words = words_to_censor.read().rstrip()
    bad_words_list = bad_words.split("\n")
    bad_words_set = {bad_word.lower() for bad_word in bad_words_list}
    new_lines = []  # New list of new lines (redacted or not)
    for line in file_to_censor:
        words = line.split()  # This creates a new list of words each line
        new_line = ""  # New line to add to the new_lines list
        for word in words:  # It iterates through each word of the line
            word = word.lower()  # Lowercase the word
            if word.lower() in bad_words_set:
                redacted_word = "*" * len(word)
                new_line += redacted_word + " "
            else:
                new_line += word + " "
        new_lines.append(new_line.rstrip())
    for line in new_lines:
        redacted_file.write(line + "\n")


if __name__ == "__main__":
    try:
        file_to_censor = open(input("File to censor: "), "r")
        words_to_censor = open(input("File of censored words: "), "r")
        redacted_file = open(input("Name of new file: "), "w")
        censor_file(file_to_censor, words_to_censor, redacted_file)
        file_to_censor.close()
        words_to_censor.close()
        redacted_file.close()
    except FileNotFoundError:
        print("File not found")