import random, string


def generate_random_password() -> str:
    password_length = random.randrange(7, 11)
    characters = string.ascii_letters + string.digits
    password = ""
    for index in range(password_length):
        password = password + random.choice(characters)
    return password

if __name__ == "__main__":
    password = generate_random_password()
    print(password)
