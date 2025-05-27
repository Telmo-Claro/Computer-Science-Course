import json


def open_json():
    with open("movies.json", "r", encoding="utf8") as json_file:
        movies_data = json.load(json_file)
        return movies_data


def movie_overview():
    movies_data = open_json()
    number_of_movies_2004 = 0
    sf_total = 0
    keanu_reeves_baby_boo = 0
    stallone = 0
    for item in movies_data:
        if item["year"] == 2004:
            number_of_movies_2004 += 1
        if "Science Fiction" in item["genres"]:
            sf_total += 1
        if "Keanu Reeves" in item["cast"]:
            keanu_reeves_baby_boo += 1
            print(item)
        if "Sylvester Stallone" in item["cast"] and 1995 <= item["year"] <= 2005:
            stallone += 1
            print(item)

    return number_of_movies_2004, sf_total, keanu_reeves_baby_boo, stallone


def change_stuff():
    movies_data = open_json()
    out_file = open("movies.json", "w", encoding="utf8")
    for movie in movies_data:
        if movie["title"] == "Gladiator":
            movie["year"] = 2001
        if "Natalie Portman" in movie["cast"]:
            for item in movie["cast"]:
                if item == "Natalie Portman":
                    movie["cast"] = ["Nat Portman" if actor == "Natalie Portman" else actor for actor in movie["cast"]]
        if "Kevin Spacey" in movie["cast"]:
            for item in movie["cast"]:
                if item == "Kevin Spacey":
                    movie["cast"].remove(item)
        if movie["year"] == 1900:
            movie["year"] = 1899
    json.dump(movies_data, out_file)
    out_file.close()


def get_movie(user_movie):
    movies_data = open_json()
    for item in movies_data:
        if item["title"].lower() == user_movie:
            return item


def modify_movie():
    movies_data = open_json()
    out_file = open("movies.json", "w", encoding="utf8")
    movie_to_change = input("Movie to modify: ")
    new_name = input("New name: ")
    new_year = int(input("New year: "))
    for movie in movies_data:
        if movie["title"] == movie_to_change:
            movie["title"] = new_name
            movie["year"] = new_year
            print(movie)
    json.dump(movies_data, out_file)
    out_file.close()


def main():
    while True:
        print("[I] Movie information overview")
        print("[M] Make modification based on assignment")
        print("[S] Search a movie title ")
        print("[C] Change title and/or release year by search on title")
        print("[Q] Quit program")
        user_input = input("Select: ").lower()
        if user_input == "i":
            print(movie_overview())
        if user_input == "m":
            change_stuff()
        if user_input == "s":
            print(get_movie(user_movie=input("Search Movie: ").lower()))
        if user_input == "c":
            modify_movie()
        if user_input == "q":
            break


if __name__ == "__main__":
    main()