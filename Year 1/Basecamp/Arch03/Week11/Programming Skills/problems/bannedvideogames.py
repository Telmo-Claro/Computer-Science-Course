import csv


def open_file():
    with open('bannedvideogames.csv', "r", encoding="utf8") as csv_read:
        banned_games_reader = csv.DictReader(csv_read,
                                             fieldnames=['Id', 'Game', 'Series', 'Country', 'Details', 'Ban Category',
                                                         'Ban Status', 'Wikipedia Profile', 'Image', 'Summary',
                                                         'Developer', 'Publisher', 'Genre', 'Homepage'])
        banned_games_reader = [row for row in banned_games_reader]
        return banned_games_reader


def print_request():
    banned_games = open_file()
    banned_israel = 0
    most_bans = {}
    haxaxin = 0
    germany_bans = []
    countries_red_dead = []
    for game in banned_games:
        if game["Country"] == "Israel":
            banned_israel += 1
            print(game)
        if game["Country"] in most_bans:
            most_bans[game["Country"]] += 1
        else:
            most_bans[game["Country"]] = 1
        if game["Series"] == "Assassin's Creed" and game["Ban Status"] == "Active":
            haxaxin += 1
        if game["Country"] == "Germany":
            germany_bans.append(game)
        if game["Game"] == "Red Dead Redemption":
            countries_red_dead.append(game)
    sorted_most_bans = sorted(most_bans.items(), key=lambda x: x[1], reverse=True)
    return banned_israel, sorted_most_bans[0], haxaxin, germany_bans, countries_red_dead


def banned_per_country():
    banned_games = open_file()
    countries = []
    banned_games_per_country = {}
    for item in banned_games:
        if item["Country"] not in countries:
            if item["Country"] == "Country":
                continue
            countries.append(item["Country"])
    ordered_countries = sorted(countries, key=str.lower)
    for country in ordered_countries:
        list_of_games = []
        for game in banned_games:
            if country == game["Country"]:
                list_of_games.append(game)
        banned_games_per_country[country] = list_of_games
    for item in banned_games_per_country.values():
        for key, value in banned_games_per_country.items():
            print(key, "-", len(item))
            for game in item:
                print(game["Game"])


def dataset_by_country():
    user_input = input("Enter a country: ").lower()
    banned_games = open_file()
    for game in banned_games:
        if game["Country"].lower() == user_input:
            print(game["Game"], "-", game["Details"])
        else:
            continue


def modifications():
    banned_games = open_file()
    updated_banned = []
    for game in banned_games:
        if game["Country"] == "Germany":
            continue
        if game["Game"] == "Silent Hill VI":
            game["Game"] = "Silent Hill Remastered"
        if game["Country"] == "Brazil" and game["Game"] == "Bully":
            game["Ban Status"] = "Ban Lifted"
        if game["Game"] == "Manhunt II":
            game["Genre"] = "Action"
        updated_banned.append(game)

    with open("bannedvideogames.csv", "w", encoding="utf8", newline='') as banned_games_writer:
        fieldnames = ['Id', 'Game', 'Series', 'Country', 'Details', 'Ban Category', 'Ban Status', 'Wikipedia Profile',
                      'Image', 'Summary', 'Developer', 'Publisher', 'Genre', 'Homepage']
        writer = csv.DictWriter(banned_games_writer, fieldnames=fieldnames)
        writer.writerows(updated_banned)


def add_game():
    game_id = input("Enter a game ID: ")
    game = input("Enter a game name: ")
    series = input("Enter a series: ")
    country = input("Enter a country: ")
    details = input("Enter a details: ")
    category = input("Enter a category: ")
    ban_status = input("Enter a ban status: ")
    wikipedia_profile = input("Enter a Wikipedia profile: ")
    image = input("Enter a image: ")
    summary = input("Enter a summary: ")
    developer = input("Enter a developer: ")
    publisher = input("Enter a publisher: ")
    genre = input("Enter a genre: ")
    homepage = input("Enter a homepage: ")
    new_game = [game_id, game, series, country, details, category, ban_status, wikipedia_profile, image, summary,
                developer, publisher, genre, homepage]
    with open("bannedvideogames.csv", "a", encoding="utf8", newline='') as banned_games_writer:
        writer = csv.writer(banned_games_writer)
        writer.writerow(new_game)


def main():
    while True:
        print("[I] Print request info from assignment")
        print("[M] Make modification based on assignment")
        print("[A] Add new game to list")
        print("[O] Overview of banned games per country")
        print("[S] Search the dataset by country")
        print("[Q] Quit program")
        user_input = input("Select: ").lower()
        if user_input == "i":
            print(print_request())
        if user_input == "m":
            modifications()
        if user_input == "a":
            add_game()
        if user_input == "o":
            banned_per_country()
        if user_input == "s":
            dataset_by_country()
        if user_input == "q":
            break


if __name__ == "__main__":
    main()
