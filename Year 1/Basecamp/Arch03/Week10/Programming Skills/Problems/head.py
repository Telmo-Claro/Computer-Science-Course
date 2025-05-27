import sys


def show_first_ten(file):
    try:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines[:10]:
                print(line, end="")
    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    show_first_ten(sys.argv[1])
