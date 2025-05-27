def comment_checker(*files_to_read):
    for file in files_to_read:
        file_name = file
        try:
            with open(file) as file:
                prevLine = "Placeholder"
                line_count = 1
                for line in file:
                    if len(line) > 1:
                        line = line.split()
                        if "def" in line[0]:
                            if "#" in prevLine[0]:
                                prevLine = " ".join(line)
                                line_count += 1
                                continue
                            else:
                                print(
                                    f"""File: {file_name} contains a function [{''.join(line).removesuffix(':').removeprefix('def')}] on line [{line_count}] without a preceding comment.""")
                                prevLine = " ".join(line)
                                line_count += 1
                        else:
                            line_count += 1
                            prevLine = " ".join(line)
                    else:
                        line_count += 1
        except FileNotFoundError:
            print("File not found", file)
            exit()


if __name__ == "__main__":
    input_files = input("")
    input_files = input_files.split(",")
    list_of_files = []
    for file in input_files:
        file = file.strip()
        list_of_files.append(file)
    for file in list_of_files:
        comment_checker(file)
    # comment_checker(input_files)
    # randomtext.txt, new_text.txt
