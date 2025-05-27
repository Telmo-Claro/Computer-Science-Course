import random
from colorama import Fore
import json
import time

# query questions
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

# Define the indexes
indexes = [
    (9, 28), (9, 25), (9, 22), (9, 19), (9, 16), (9, 13), (9, 10), (9, 7), (9, 4), (9, 1),
    (8, 1), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1),
    (0, 4), (0, 7), (0, 10), (0, 13), (0, 16), (0, 19), (0, 22), (0, 25), (0, 28),
    (1, 28), (2, 28), (3, 28), (4, 28), (5, 28), (6, 28), (7, 28), (8, 28)
]

player = {
    "name1": "",
    "name2": ""
}
#player1
p1 = {
    "name": "",
    "index": 0,
    "balance": 0,
    "inventory": {
        "keyboard": 0,
        "mouse": 0,
        "monitor": 0,
        "printer": 0,
        "cpu": 0,
        "gpu": 0,
        "motherboard": 0,
        "minitower": 0
    }
}
#player2
p2 = {
    "name": "",
    "index": 0,
    "balance": 0,
    "inventory": {
        "keyboard": 0,
        "mouse": 0,
        "monitor": 0,
        "printer": 0,
        "cpu": 0,
        "gpu": 0,
        "motherboard": 0,
        "minitower": 0
    }
}

prizes_shop = {
    "shop1": {
        "keyboard": 50,
        "mouse": 30,
        "monitor": 130,
        "printer": 20,
        "cpu": 150,
        "gpu": 200,
        "motherboard": 75,
        "minitower": 125
    },
    "shop2": {
        "keyboard": 20,
        "mouse": 20,
        "monitor": 250,
        "printer": 10,
        "cpu": 200,
        "gpu": 250,
        "motherboard": 50,
        "minitower": 75
    }
}
nl = "\n"
# End of Indexes

# Start of variables
game_running = False
# End of variables


#First set all functions to later call them in the game.
def roll_dice(name):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print(f"{name} rolled a {d1} and a {d2}")
    return d1, d2

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

# get new index of player after rolling dices
def update_position(player_index, dice_roll):
    new_index = player_index + dice_roll
    # check if new index is > 35 (that's the last index of our board_game)
    if new_index >= len(indexes):
        new_index = new_index - len(indexes)
    return new_index

items = ("keyboard", "mouse", "monitor", "printer", "cpu", "gpu", "motherboard", "minitower")

def random_item(pl):
    rdm_item = random.choice(items)
    print(f"You've been given a {rdm_item}")
    pl["inventory"][rdm_item] += 1

def shop(pla):
    print(f"Welcome to the shop {pla['name']}.")
    if pla["index"] == 9:
        prizes = prizes_shop["shop1"]
    else:
        prizes = prizes_shop["shop2"]
    lowest_price = min(prizes.values())
    shop_open = True
    if pla["balance"] >= lowest_price:
        while shop_open:
            offer = input("Would you like to buy something? Y/N")
            if offer.lower() == "y" or offer.lower() == "yes":
                print("You have enough balance to scoop some:")
                for item, price in prizes.items():
                    if pla["balance"] >= price:
                        print(f"- {item} for {price} florins")
                while True:
                    offer1 = input("What would you like to buy?")
                    if offer1.lower() not in items:
                        print("Enter a right computer part")
                    else:
                        pla["balance"] -= prizes[offer1]
                        pla["inventory"][offer1] += 1
                        print(f"""You successfully bought a {offer1}""")
                        shop_open = False
                        break
            elif offer.lower() == "n" or offer.lower() == "no":
                print("Thanks for having you in the shop!")
                break
            else:
                print("Please enter Y/N")
    else:
        print("You don't have enough balance to buy anything from the shop.")
        

def field_check(p):
    if p["index"] == 16 or p["index"] == 34:
        random_item(p)
    elif p["index"] == 2 or p["index"] == 20:
        print("Event")
    elif p["index"] == 5 or p["index"] == 14 or p["index"] == 23 or p["index"] == 32:
        print("Query")
    elif p["index"] == 7 or p["index"] == 25:
        print("You encountered a famous person")
    elif p["index"] == 9 or p["index"] == 27:
        shop(p)
    elif p["index"] == 11 or p["index"] == 29:
        print("You've been given a chance")
    elif p["index"] == 18:
        print("You're in jail")

def simulate_round():
    # global p1, p2
    if p1["name"][-1].lower() == "s" or p1["name"][-1].lower() == "x":
        print(f"{p1['name']}' turn")
    else:
        print(f"{p1['name']}'s turn")
    roll_dices1 = input("Enter any key to roll dice: ")
    d1, d2 = roll_dice(p1["name"])
    
    # Update player 1 position
    p1["index"] = update_position(p1["index"], d1 + d2)
    p1["balance"] += d1 * d2
    field_check(p1)
    
    # exit function if p1 balance >= 5000
    if p1["balance"] >= 5000:
        return

    row_index_player1, column_index_player1 = indexes[p1["index"]]
    row_index_player2, column_index_player2 = indexes[p2["index"]]
    
    time.sleep(1)
    # Update map after move player 1
    for i, row in enumerate(map_list):
        if i == row_index_player1 == row_index_player2:
            if column_index_player1 == column_index_player2:
                if i == 0 or i == 9:
                    row = row[:column_index_player1] + 'XO' + row[column_index_player1 + 1:]
                else:
                    row = row[:column_index_player1] + 'XO' + ']' + row[column_index_player1 + 3:]
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
    print(f"Balance {p1['name']}: {p1['balance']}")
    time.sleep(1)
    if p2["name"][-1].lower() == "s" or p2["name"][-1].lower() == "x":
        print(f"{p2['name']}' turn")
    else:
        print(f"{p2['name']}'s turn")
    roll_it = input("Press any key to roll the dices ...")
    time.sleep(1)
    d3, d4 = roll_dice(p2["name"])

    # Update player 2 position
    p2["index"] = update_position(p2["index"], d3 + d4)
    p2["balance"] += d3 * d4
    field_check(p2)
    if p2["balance"] >= 5000:
        return
    row_index_player2, column_index_player2 = indexes[p2["index"]]
    
    time.sleep(1)
    # Update map after move player 2
    for i, row in enumerate(map_list):
        if i == row_index_player1 == row_index_player2:
            if column_index_player1 == column_index_player2:
                if i == 0 or i == 9:
                    row = row[:column_index_player1] + 'XO' + row[column_index_player1 + 1:]
                else:
                    row = row[:column_index_player1] + 'XO' + ']' + row[column_index_player1 + 3:]
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
    print(f"Balance {p2['name']}: {p2['balance']}")


# Set the map
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

#This will be printed - Start of the game
while True:
    print("Welcome to TUBOGA aka The Ultimate Board Game!")
    time.sleep(0.5)
    player["name1"] = input("Player one name: ").strip()
    time.sleep(0.5)
    player["name2"] = input("Player two name: ").strip()

    if player["name1"] and player["name2"] and player["name1"].lower() != player["name2"].lower():
        break
    else:
        print("Please enter a different name")


while True:
    rules = input(f"Press R to read the rules or S to start the game:\n")
    if rules.lower() == "r":
        print(f"""Goal: The goal of the game is to get rich by selling computers.\n
            The first player to collect a total of 5000 florins wins the game. \n
            You can buy and sell computer parts or full computers.\n
            You can get these parts through events or at the shops.\n
            Have fun!
            """)
        game_running = True
        break
    elif rules.lower() == "s":
        game_running = True
        break
    else:
        print("Input error")
        

while game_running:
    time.sleep(1)
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
    
    print(board_map)
    time.sleep(1)

    chooseStart = True
    while chooseStart:
        print(f"Rolling dice...")
        time.sleep(1)
        
        p1begin = random.randint(1, 6)
        print(f"{player['name1']} rolled a {p1begin}")
        time.sleep(1)
        
        print(f"Rolling dice...")
        time.sleep(1)
        
        p2begin = (random.randint(1, 6))
        print(f"{player['name2']} rolled a {p2begin}")
        
        if p1begin > p2begin:
            chooseStart = False
            p1["name"] = player["name1"]
            p2["name"] = player["name2"]
        elif p1begin < p2begin:
            chooseStart = False
            p2["name"] = player["name1"]
            p1["name"] = player["name2"]
        else:
            time.sleep(1)
            print("Let's try again!")
    print(f"{p1['name']} starts the game!")
    
    while True:
        simulate_round()
        if p1["balance"] >= 5000:
            print("Player1 won the match")
            exit()
        if p2["balance"] >= 5000:
            print("Player2 won the match")
            exit()