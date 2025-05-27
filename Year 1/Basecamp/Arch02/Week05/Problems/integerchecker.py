def is_integer(unchecked: str) -> bool:
    if (
        len(unchecked) >= 1
        and unchecked.isdigit()
        or unchecked[0] == "+"
        and unchecked[1:].isdigit()
        or unchecked[0] == "-"
        and unchecked[1:].isdigit()
    ):
        return True
    else:
        return False


# ChatGPTed cause i didn't understand
def remove_non_integer(unchecked: str) -> int:
    solution_result = ""
    for char in unchecked:
        if char.isdigit() or (char in ["+", "-"] and len(solution_result) == 0):
            solution_result += char
    if len(solution_result) == 0:
        return 0
    return int(solution_result)


if __name__ == "__main__":
    unchecked = input("Enter a string: ").strip().upper()
    if is_integer(unchecked):
        print("valid")
    else:
        print("invalid")
    solution_result = remove_non_integer(unchecked)
    print(solution_result)
