def get_most_words(file_to_read, file_to_write):
    try:
        with open(file_to_read) as file_to_read:
            with open(file_to_write, "w") as file_to_write:
                for lines in file_to_read:
                    lines = lines.rsplit()
                    if "#" not in lines:
                        file_to_write.write(" ".join(lines))
                        file_to_write.write("\n")
    except FileNotFoundError:
        print("File not found", file_to_read)
        exit()


if __name__ == "__main__":
    get_most_words("randomtext.txt", "new_text.txt")
