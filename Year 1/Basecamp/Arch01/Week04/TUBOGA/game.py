import random
from colorama import Fore
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
    },{
        "question": "Who is often referred to as the 'father of the computer'?",
        "options": ["A) Steve Jobs", "B) Alan Turing", "C) Bill Gates", "D) Tim Berners-Lee"],
        "correct_answer": "B) Alan Turing"
    },
    {
        "question": "What does HTML stand for?",
        "options": ["A) Hyper Text Markup Language", "B) High Tech Machine Learning", "C) Home Tool Maintenance Library", "D) Human Technology Management Link"],
        "correct_answer": "A) Hyper Text Markup Language"
    },
    {
        "question": "Which programming language is commonly used for artificial intelligence and machine learning?",
        "options": ["A) Java", "B) Python", "C) C++", "D) Ruby"],
        "correct_answer": "B) Python"
    },
    {
        "question": "Who co-founded Apple Inc. alongside Steve Jobs?",
        "options": ["A) Larry Page", "B) Bill Gates", "C) Steve Wozniak", "D) Mark Zuckerberg"],
        "correct_answer": "C) Steve Wozniak"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A) Computer Power Unit", "B) Central Processing Unit", "C) Core Programming Utility", "D) Computing and Processing Undertaking"],
        "correct_answer": "B) Central Processing Unit"
    },
    {
        "question": "Who is the CEO of Tesla and SpaceX?",
        "options": ["A) Jeff Bezos", "B) Tim Cook", "C) Elon Musk", "D) Sundar Pichai"],
        "correct_answer": "C) Elon Musk"
    },
    {
        "question": "Which of the following is not a type of cloud computing service?",
        "options": ["A) SaaS (Software as a Service)", "B) PaaS (Platform as a Service)", "C) MaaS (Mobile as a Service)", "D) IaaS (Infrastructure as a Service)"],
        "correct_answer": "C) MaaS (Mobile as a Service)"
    },
    {
        "question": "Who invented the World Wide Web (WWW)?",
        "options": ["A) Larry Page", "B) Al Gore", "C) Tim Berners-Lee", "D) Sergey Brin"],
        "correct_answer": "C) Tim Berners-Lee"
    },
    {
        "question": "Which company developed the Java programming language?",
        "options": ["A) Microsoft", "B) Apple", "C) Sun Microsystems", "D) IBM"],
        "correct_answer": "C) Sun Microsystems"
    },
    {
        "question": "What is the purpose of a VPN (Virtual Private Network)?",
        "options": ["A) To speed up internet connection", "B) To protect user privacy and security", "C) To create virtual reality environments", "D) To enhance computer graphics performance"],
        "correct_answer": "B) To protect user privacy and security"
    },
    {
        "question": "Who is the founder of Amazon.com?",
        "options": ["A) Jeff Bezos", "B) Elon Musk", "C) Larry Ellison", "D) Mark Zuckerberg"],
        "correct_answer": "A) Jeff Bezos"
    },
    {
        "question": "Which of the following is a popular version control system used in software development?",
        "options": ["A) CVS", "B) SVN", "C) Git", "D) Mercurial"],
        "correct_answer": "C) Git"
    },
    {
        "question": "Who is the creator of the Linux operating system?",
        "options": ["A) Linus Torvalds", "B) Richard Stallman", "C) Steve Jobs", "D) Bill Gates"],
        "correct_answer": "A) Linus Torvalds"
    },
    {
        "question": "Which company developed the Android operating system?",
        "options": ["A) Apple", "B) Microsoft", "C) Google", "D) Samsung"],
        "correct_answer": "C) Google"
    },
    {
        "question": "What does SSD stand for in the context of computer hardware?",
        "options": ["A) Secure Storage Device", "B) Solid-State Drive", "C) Serial System Disk", "D) Software Storage Directory"],
        "correct_answer": "B) Solid-State Drive"
    },
    {
        "question": "Who is the current CEO of Microsoft?",
        "options": ["A) Tim Cook", "B) Satya Nadella", "C) Bill Gates", "D) Steve Ballmer"],
        "correct_answer": "B) Satya Nadella"
    },
    {
        "question": "What is the primary function of a firewall in computer networking?",
        "options": ["A) To block unwanted websites", "B) To prevent unauthorized access to or from a private network", "C) To boost internet speed", "D) To enhance Wi-Fi signal strength"],
        "correct_answer": "B) To prevent unauthorized access to or from a private network"
    },
    {
        "question": "Who is known as the co-founder of Reddit?",
        "options": ["A) Mark Zuckerberg", "B) Steve Huffman", "C) Larry Page", "D) Jack Dorsey"],
        "correct_answer": "B) Steve Huffman"
    },
    {
        "question": "Which programming language is commonly used for web development and design?",
        "options": ["A) COBOL", "B) Fortran", "C) JavaScript", "D) Pascal"],
        "correct_answer": "C) JavaScript"
    },
    {
        "question": "Who is credited with the invention of the first graphical web browser?",
        "options": ["A) Marc Andreessen", "B) Tim Berners-Lee", "C) Larry Page", "D) Sergey Brin"],
        "correct_answer": "A) Marc Andreessen"
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
    "sign": "X",
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
    "sign": "O",
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

# End of Indexes

# Start of variables
game_running = False
lines = "------------------------"
reset = Fore.RESET
# End of variables



#First set all functions to later call them in the game.
def roll_dice(name):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print("\nDices rolling...")
    time.sleep(1)
    print(f"\n{name} rolled a {d1}")
    time.sleep(1)
    print(f"\nand a {d2}")
    time.sleep(1.5)
    return d1, d2

def pay_your_tax(player):
    print("Well well well")
    print("\n")
    time.sleep(3)
    print("Look who we have here.")
    print("\n")
    time.sleep(3)
    print("Let me take 25 percent of your forins for taxes.")
    print("\n")
    tax = round(player["balance"] * .25, 2)
    time.sleep(2.5)
    print("*Grabbing your money*")
    print("\n")
    time.sleep(2)
    player["balance"] -= tax
    print(f"Thank you for your {tax} forins. Enjoy your game ;)")


def field_check(player):
    index = player["index"]
    
    if index in [16, 34]:
        random_item(player)
    elif index == 0:
        time.sleep(2)
        print(f"\nYou're getting 200 florins for getting on the START")
        player["balance"] += 200
        time.sleep(2)
    elif index in [2, 20]:
        pay_your_tax(player)
    elif index in [5, 14, 23, 32]:
        query(player)
    elif index in [7, 25]:
        print("\nYou encountered a famous person")
        famous_person(player)
    elif index in [9, 27]:
        shop(player)
    # elif index in [11, 29]:
    #     print("You've been given a chance")
    elif index == 18:
        rew = random.randint(1,300)
        player["balance"] += rew
        print(f"{rew} Florins for you")


def query(player):
    random_question = random.choice(questions)

    question = random_question['question']
    options = random_question['options']
    correct_answer = random_question['correct_answer']
    time.sleep(1.5)
    print("\n")
    print(question)
    print("\n")

    for option in options:
        time.sleep(1)
        print(option)
    print(lines)
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
        player["balance"] += reward
        time.sleep(2.5)
        print(f"Correct! {player['name']} earned {reward} Florin")
    else:
        time.sleep(2.5)
        print("Wrong! The correct answer is:", correct_answer)

# get new index of player after rolling dices
def update_position(player_index, dice_roll):
    new_index = player_index + dice_roll
    # check if new index is > 35 (that's the last index of our board_game)
    if new_index >= len(indexes):
        new_index = new_index - len(indexes)
    return new_index

items = ("keyboard", "mouse", "monitor", "printer", "cpu", "gpu", "motherboard", "minitower")

def random_item(player):
    time.sleep(2)
    print(f"\n{player['name']} is getting a free random item.")
    time.sleep(2)
    rdm_item = random.choice(items)
    player["inventory"][rdm_item] += 1
    print(f"\nYou've been given a {rdm_item}")
    time.sleep(1.5)

def has_all_parts(player):
    for item in player["inventory"].values():
        if item == 0:
            return False
    return True

def famous_person(player):
    query(player)
    if has_all_parts(player):
        selling_price = random.randint(1000, 1500)
        while True:
            selling = input(f"Would you like to sell your computer to this famous person for {selling_price} florins? Y/N: ")
            if selling.lower() in ["y", "yes"]:
                for item in player["inventory"].values():
                    item -= 1
                player["balance"] += selling_price
                print(f"You successfully sold your pc for {selling_price} florins. Goodbye!")
                break
            elif selling.lower() in ["n", "no"]:
                print("Also good, goodbye!")
                break
            else:
                print("Please enter Y/N")

def shop(player):
    time.sleep(2)
    print(f"\nWelcome to the shop {player['name']}.")
    print(f"Your inventory {player['inventory']}")
    prizes = prizes_shop["shop1"] if player["index"] == 9 else prizes_shop["shop2"]
    lowest_price = min(prizes.values())
    shop_open = True

    if player["balance"] >= lowest_price:
        while shop_open:
            time.sleep(2)
            print("\nYou have enough balance to scoop some:\n")
            
            # Iterate over price list
            for item, price in prizes.items():
                if player["balance"] >= price:
                    print(f"- {item} for {price} florins")
                    time.sleep(1)
            print(lines)
            offer = input("\nWould you like to buy something? Y/N: ")
            if offer.lower() in ["n", "no"]:
                if has_all_parts(player):
                    sell_price = random.randint(850, 1200)
                    sell = input(f"\nDo you want to sell a computer for {sell_price}? Y/N: ")
                    if sell.lower() in ["y", "yes"]:
                        for item in player["inventory"].values():
                            item -= 1
                    player["balance"] += sell_price
                    time.sleep(2)
                    print(f"\nYou successfully sold your computer for {sell_price} florins.\nThanks for shopping with us!")
                    shop_open = False
                    break
                else:
                    print("Thanks for having you, bye!")
                    shop_open = False
                    break
            if offer.lower() in ["y", "yes"]:
                while True:
                    offer1 = input("\nWhat would you like to buy?\nEnter 'exit' if you want to exit the shop. ")
                    if offer1.lower() not in items:
                        print("\nEnter an available computer part")
                    elif offer1.lower() == "exit":
                        print("\nThanks for shopping with us!")
                        shop_open = False
                        break
                    else:
                        if player["balance"] >= prizes[offer1]:
                            player["balance"] -= prizes[offer1]
                            player["inventory"][offer1] += 1
                            time.sleep(2)
                            print(f"\nYou successfully bought a {offer1}.\nThanks for shopping with us!")
                            if has_all_parts(player):
                                sell_price = random.randint(850, 1200)
                                sell = input(f"\nDo you want to sell a computer for {sell_price}? Y/N: ")
                                if sell.lower() in ["y", "yes"]:
                                    for item in player["inventory"].values():
                                        item -= 1
                                    player["balance"] += sell_price
                                    time.sleep(2)
                                    print(f"\nYou successfully sold your computer for {sell_price} florins.\nThanks for shopping with us!")
                                    shop_open = False
                                    break
                            else:
                                shop_open = False
                                break
                        else:
                            print(f"\nYou don't have enough money for this {offer1}")        
            elif offer.lower() in ["n", "no"]:
                print("Thanks for having you, bye!")
                shop_open = False
                break
            else:
                print("Input error. Enter: Y/N ")
    else:
        time.sleep(2)
        print("\nYou don't have enough balance to buy anything from the shop.\nBye!")

def simulate_round():
    time.sleep(1.5)
    if p1["name"][-1].lower() == "s" or p1["name"][-1].lower() == "x":
        print(f"\n{p1['name']}' turn ({Fore.GREEN + p1['sign'] + reset})")
    else:
        print(f"\n{p1['name']}'s turn ({Fore.GREEN + p1['sign'] + reset})")
    roll_dices1 = input("\nPress enter to roll dice: ")
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
    print("\n")
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
                    row = row[:column_index_player1]+ 'X' + row[column_index_player1 + 1:]
                    row = row[:column_index_player2] + 'O' + row[column_index_player2 + 1:]
                else:
                    row = row[:column_index_player1] + 'X' + ']' + row[column_index_player1 + 2:]
                    row = row[:column_index_player2] + 'O' + ']' + row[column_index_player2 + 2:]
        elif i == row_index_player1:
            row = row[:column_index_player1] + 'X'+ row[column_index_player1 + 1:]
        elif i == row_index_player2:
            row = row[:column_index_player2] + 'O' + row[column_index_player2 + 1:]
        print(row)
    time.sleep(1.5)
    print(f"\nBalance {p1['name']}: {p1['balance']}")
    print(lines)
    time.sleep(1.5)
    if p2["name"][-1].lower() == "s" or p2["name"][-1].lower() == "x":
        print(f"\n{p2['name']}' turn ({Fore.RED + p2['sign'] + reset})")
    else:
        print(f"\n{p2['name']}'s turn ({Fore.RED + p2['sign'] + reset})")
    roll_it = input("\nPress any key to roll the dices ...")
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
    print("\n")
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
                    row = row[:column_index_player1]+ 'X' + row[column_index_player1 + 1:]
                    row = row[:column_index_player2] + 'O' + row[column_index_player2 + 1:]
                else:
                    row = row[:column_index_player1] + 'X' + ']' + row[column_index_player1 + 2:]
                    row = row[:column_index_player2] + 'O' + ']' + row[column_index_player2 + 2:]
        elif i == row_index_player1:
            row = row[:column_index_player1] + 'X'+ row[column_index_player1 + 1:]
        elif i == row_index_player2:
            row = row[:column_index_player2] + 'O' + row[column_index_player2 + 1:]
        print(row)
    time.sleep(1.5)
    print(f"\nBalance {p2['name']}: {p2['balance']}")
    print(lines)


# Set the map
map_list = [
    "[M][ ][E][ ][ ][Q][ ][F][ ][P]",
    "[ ]                        [ ]",
    "[R]                        [ ]",
    "[ ]                        [ ]",
    "[Q]                        [ ]",
    "[ ]                        [Q]",
    "[ ]                        [ ]",
    "[ ]                        [R]",
    "[ ]                        [ ]",
    "[P][ ][F][ ][ ][ ][ ][E][ ][S]"
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
        time.sleep(4)
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
        print(f"\nRolling dice...")
        time.sleep(1)
        
        p1begin = random.randint(1, 6)
        print(f"\n{player['name1']} rolled a {p1begin}")
        time.sleep(1)
        
        print(f"\nRolling dice...")
        time.sleep(1)
        
        p2begin = (random.randint(1, 6))
        print(f"\n{player['name2']} rolled a {p2begin}")
        
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
            print("\nLet's try again!")
    time.sleep(1)
    print(f"\n{p1['name']} starts the game!")
    time.sleep(1)
    print(f"\n{p1['name']} is {Fore.GREEN + 'X' + reset} and {p2['name']} is {Fore.RED + 'O' + reset} on the playboard.")
    time.sleep(3)
    
    while True:
        simulate_round()
        if p1["balance"] >= 5000:
            print("Player1 won the match")
            game_running = False
            break
        if p2["balance"] >= 5000:
            print("Player2 won the match")
            game_running = False
            break