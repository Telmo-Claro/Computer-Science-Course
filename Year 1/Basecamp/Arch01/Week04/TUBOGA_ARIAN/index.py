import random
from colorama import Fore
import json
import time

questions = [
    {
        "question": "What is the output of the following code snippet?\n\n```\nprint(2 + 3 * 4)\n```",
        "options": ["A) 14", "B) 20", "C) 26", "D) 10"],
        "correct_answer": "A) 14"
    },
    {
        "question": "Which of the following is a correct way to start a Python comment?",
        "options": ["A) //", "B) #", "C) <!--", "D) --"],
        "correct_answer": "B) #"
    },
    {
        "question": "What is the output of the following code snippet?\n\n```\nprint('hello' * 3)\n```",
        "options": ["A) hellohellohello", "B) hello hello hello", "C) hello3", "D) Error"],
        "correct_answer": "A) hellohellohello"
    },
    {
        "question": "Which of the following data types is immutable in Python?",
        "options": ["A) List", "B) Tuple", "C) Dictionary", "D) Set"],
        "correct_answer": "B) Tuple"
    },
    {
        "question": "What will be the value of `x` after the following code is executed?\n\n```\nx = 10\nx += 5\n```",
        "options": ["A) 10", "B) 15", "C) 5", "D) Error"],
        "correct_answer": "B) 15"
    },
    {
        "question": "Which of the following methods removes the last element from a list in Python?",
        "options": ["A) pop()", "B) remove()", "C) del()", "D) clear()"],
        "correct_answer": "A) pop()"
    },
    {
        "question": "What does the `len()` function do in Python?",
        "options": ["A) Returns the number of items in a list", "B) Returns the largest item in an iterable", "C) Returns the sum of all items in an iterable", "D) Returns the index of an item in a list"],
        "correct_answer": "A) Returns the number of items in a list"
    },
    {
        "question": "Which of the following is not a valid Python variable name?",
        "options": ["A) my_variable", "B) _variable123", "C) 123_variable", "D) variable-123"],
        "correct_answer": "D) variable-123"
    },
    {
        "question": "What is the result of the expression `3 * 'abc'`?",
        "options": ["A) abcabcabc", "B) abc * 3", "C) abcabc", "D) Error"],
        "correct_answer": "A) abcabcabc"
    },
    {
        "question": "What does the `range()` function return in Python?",
        "options": ["A) A list of integers", "B) A tuple of integers", "C) A dictionary of integers", "D) An iterator"],
        "correct_answer": "D) An iterator"
    }
]

def roll_dice(playerName):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print("Rolling dices ...")
    time.sleep(2)
    print(f"{playerName} rolled a {d1} and a {d2}")
    time.sleep(2)
    return d1, d2

map_list = [
    "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]"
]

map_start = [
    "[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ]                        [ ]",
    "[ ][ ][ ][ ][ ][ ][ ][ ][ ][XO]"
]

# Define the indexes
indexes = [
    (9, 28), (9, 25), (9, 22), (9, 19), (9, 16), (9, 13), (9, 10), (9, 7), (9, 4), (9, 1),
    (8, 1), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1),
    (0, 4), (0, 7), (0, 10), (0, 13), (0, 16), (0, 19), (0, 22), (0, 25), (0, 28),
    (1, 28), (2, 28), (3, 28), (4, 28), (5, 28), (6, 28), (7, 28), (8, 28)
]

player1_index = 0
player2_index = 0
player1_balance = 0
player2_balance = 0
nl = "\n"

#First set all functions to later call them in the game.
def roll_dice(playerName):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print("Rolling dices ...")
    time.sleep(2)
    print(f"{playerName} rolled a {d1} and a {d2}")
    time.sleep(2)
    return d1, d2

def update_position(player_index, dice_roll):
    new_index = player_index + dice_roll
    if new_index > len(indexes):
        new_index = (player_index + dice_roll) % len(indexes)
    return new_index

def query():
    random_question = random.choice(questions)

    question = random_question['question']
    options = random_question['options']
    correct_answer = random_question['correct_answer']

    print(question)

    for option in options:
        print(option)

    while True:
        choice = input("Enter your choice (A, B, C, D): ").upper()  # Convert the input to uppercase
        if choice not in ['A', 'B', 'C', 'D']:
            print("Invalid input. Please enter A, B, C, or D.")
            continue
        user_choice_index = ord(choice) - ord('A')
        if user_choice_index < len(options):
            break
        else:
            print("Invalid input. Please select a valid option.")
    
    user_choice = options[user_choice_index]  # Get the selected option text
    if user_choice == correct_answer:
        reward = random.randint(50, 150)
        print(f"Correct! You earned {reward} Florin")
    else:
        print("Wrong! The correct answer is:", correct_answer)

# End of functions

# Start of variables
game_running = False

# start_position = 0

# End of variables

player_naming = True
intro = True

while True:
    print("Welcome to TUBOGA aka The Ultimate Board Game!")
    time.sleep(0.5)
    p1 = input("Player one name: ").strip()
    time.sleep(0.5)
    p2 = input("Player two name: ").strip()

    if p1 and p2 and p1.lower() != p2.lower():
        break

while intro:
    print(nl)
    rules = input(f"Press R to read the rules or S to start the game:\n")

    print(nl)
    if rules.lower() == "r":
        time.sleep(3)
        print(f"""Goal:\n
            The goal of the game is to get rich by selling computers.\n
            The first player to collect a total of 5000 florins wins the game. \n
            You can buy and sell computer parts or full computers.\n
            You can get these parts through events or at the shops.\n
            Have fun!
            """)
        time.sleep(3)
        game_running = True
        break
    elif rules.lower() == "s":
        game_running = True
        break
    else:
        print("Input error")


while game_running:
    
    board_map = (
    "[J][ ][E][ ][ ][Q][ ][F][ ][X]\n"
    "[ ]                        [ ]\n"
    "[R]                        [C]\n"
    "[ ]                        [ ]\n"
    "[Q]                        [ ]\n"
    "[ ]                        [Q]\n"
    "[ ]                        [ ]\n"
    "[C]                        [R]\n"
    "[ ]                        [ ]\n"
    "[X][ ][F][ ][Q][ ][ ][E][ ][S]")
    
    
    
    chooseStart = True
    while chooseStart:
        print(f"Dice rolling...")
        time.sleep(1.5)
        
        p1begin = (random.randint(1, 6))
        print(f"{p1} rolled a {p1begin}")
        time.sleep(1)
        
        print("Dice rolling...")
        time.sleep(1.5)      
        
        p2begin = (random.randint(1, 6))
        print(f"{p2} rolled a {p2begin}")
        
        if p1begin > p2begin:
            chooseStart = False
            p1 = p1
            p2 = p2
        elif p1begin < p2begin:
            chooseStart = False
            p1 = p2
            p2 = p1
        else:
            print("Let's try again!")
    time.sleep(1.5)
    
    print(f"{p1} starts the game!")
    time.sleep(1.5)
    for i in map_start:
        print(i)

    while True:
        def simulate_round():
            global player1_index, player2_index, player1_balance, player2_balance
            if p1[-1].lower() == "s" or p1[-1].lower() == "x":
                print(f"{p1}' turn")
            else:
                print(f"{p1}'s turn")
            roll_dices1 = input("Enter any key to roll dice: ")
            d1, d2 = roll_dice(p1)

            # Update player 1 position
            player1_index = update_position(player1_index, d1 + d2)
            player1_balance += d1 * d2
            print(f"Balance {p1}: {player1_balance}")

            if player1_balance >= 5000:
                return

            # Declare indexes for players
            if player1_index > len(indexes):
                index = player1_index
                player1_index = index % len(indexes)
            row_index_player1, column_index_player1 = indexes[player1_index]
            row_index_player2, column_index_player2 = indexes[player2_index]

            time.sleep(3)
            # Update map after move player 1
            for i, row in enumerate(map_list):
                    if i == row_index_player1 == row_index_player2:
                        if column_index_player1 == column_index_player2:
                            if i == 0 or i == 9:
                                row = row[:column_index_player1] + 'XO' + row[column_index_player1 + 1:]
                            else:
                                row = row[:column_index_player1] + 'XO' + ']' + row[column_index_player1 + 2:]
                        else:
                            if i == 0 or i == 9:
                                row = row[:column_index_player1] + 'X' + row[column_index_player1 + 1:]
                                row = row[:column_index_player2] + 'O' + row[column_index_player2 + 1:]
                            else:
                                row = row[:column_index_player1] + 'X' + ']' + row[column_index_player1 + 2:]
                                row = row[:column_index_player2] + 'O' + ']' + row[column_index_player2 + 2:]
                    elif i == row_index_player1:
                        row = row[:column_index_player1] + 'X' + row[column_index_player1 + 1:]
                    elif i == row_index_player2:
                        row = row[:column_index_player2] + 'O' + row[column_index_player2 + 1:]
                    print(row)
                    
            
                
            time.sleep(1.5)
            if p2[-1].lower() == "s" or p2[-1].lower() == "x":
                print(f"{p2}' turn")
            else:
                print(f"{p2}'s turn")
            roll_it = input("Press any key to roll the dices ...")
            time.sleep(1.5)
            d3, d4 = roll_dice(p2)
            # Update player 2 position
            player2_index = update_position(player2_index, d3 + d4)
            player2_balance += d3 * d4
            print(f"Balance {p2}: {player2_balance}")
            if player2_balance >= 5000:
                return
            if player2_index > len(indexes):
                index = player2_index
                player2_index = index % len(indexes)
            row_index_player2, column_index_player2 = indexes[player2_index]

            time.sleep(2)
            # Update map after move player 2
            for i, row in enumerate(map_list):
                    if i == row_index_player1 == row_index_player2:
                        if column_index_player1 == column_index_player2:
                            if i == 0 or i == 9:
                                row = row[:column_index_player1] + 'XO' + row[column_index_player1 + 1:]
                            else:
                                row = row[:column_index_player1] + 'XO' + ']' + row[column_index_player1 + 2:]
                        else:
                            if i == 0 or i == 9:
                                row = row[:column_index_player1] + 'X' + row[column_index_player1 + 1:]
                                row = row[:column_index_player2] + 'O' + row[column_index_player2 + 1:]
                            else:
                                row = row[:column_index_player1] + 'X' + ']' + row[column_index_player1 + 2:]
                                row = row[:column_index_player2] + 'O' + ']' + row[column_index_player2 + 2:]
                    elif i == row_index_player1:
                        row = row[:column_index_player1] + 'X' + row[column_index_player1 + 1:]
                    elif i == row_index_player2:
                        row = row[:column_index_player2] + 'O' + row[column_index_player2 + 1:]
                    print(row)
                
        simulate_round()
        if player1_balance >= 5000:
            exit()
        if player2_balance >= 5000:
            print("Player2 won the match")
            exit()

        

            
        