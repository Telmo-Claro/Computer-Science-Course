import sys


def show_last_ten(file):
    list_of_lines = []
    try:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                list_of_lines.append(line.rstrip())
    except FileNotFoundError:
        print("File not found")
    print("\n".join(list_of_lines[-10:]))


if __name__ == "__main__":
    show_last_ten(input("Enter the file name: "))       
