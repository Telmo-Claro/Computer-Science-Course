if __name__ == "__main__":
    file_to_read = input(r"Enter the name of the file to read: ")
    file_to_make = input(r"Enter the name of the file to make: ")
    with open(file_to_read, "r") as file_to_read:
        with open(file_to_make, "w") as file_to_make:
            for line_number in range(0, len(file_to_read.readlines())):
                file_to_make.write(f"{line_number}: ")