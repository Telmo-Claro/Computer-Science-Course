import random


def arithmetic_operation(arithmetic_type):
    if arithmetic_type == "summation":
        correct = 0
        incorrect = 0
        for every_digit in range(10):
            first_number = random.randrange(1, 101)
            second_number = random.randrange(1, 101)
            calculation = int(input(f"{first_number} + {second_number} = "))
            if calculation == first_number + second_number:
                correct += 1
            else:
                incorrect += 1
        print(f"You had {correct} correct and {incorrect} incorrect answers in {arithmetic_type}")
    elif arithmetic_type == "multiplication":
        correct = 0
        incorrect = 0
        for every_digit in range(10):
            first_number = random.randrange(1, 101)
            second_number = random.randrange(1, 101)
            calculation = int(input(f"{first_number} * {second_number} = "))
            if calculation == first_number * second_number:
                correct += 1
            else:
                incorrect += 1
        print(f"You had {correct} correct and {incorrect} incorrect answers in {arithmetic_type}")
    elif arithmetic_type == "subtraction":
        correct = 0
        incorrect = 0
        for every_digit in range(10):
            first_number = random.randrange(1, 101)
            second_number = random.randrange(1, 101)
            calculation = int(input(f"{first_number} - {second_number} = "))
            if calculation == first_number - second_number:
                correct += 1
            else:
                incorrect += 1
        print(f"You had {correct} correct and {incorrect} incorrect answers in {arithmetic_type}")
    else:
        return "Input Error"


if __name__ == "__main__":
    arithmetic_type = input("Arithmetic operation: ").lower().strip()
    arithmetic_operation(arithmetic_type)
