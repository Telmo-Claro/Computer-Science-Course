import os
import sys
import csv


def load_csv_file(file_name):
    file_content = []
    with open(
        os.path.join(sys.path[0], file_name), newline="", encoding="utf8"
    ) as csv_file:
        file_content = list(csv.reader(csv_file, delimiter=","))
    return file_content


def get_headers(file_content):
    headers = print(file_content[0])
    return headers


# print(get_headers(load_csv_file("netflix_titles.csv")))


def search_by_type(file_content, show_type):
    return list(filter(lambda x: x[1] == show_type, file_content))


# print(search_by_type(load_csv_file("netflix_titles.csv"),"Movie"))


def search_by_director(file_content, director):
    return list(filter(lambda x: x[3] == director, file_content))


# print(search_by_director(load_csv_file("netflix_titles.csv"), "Steven Spielberg"))


def get_directors(file_content):
    directors_set = []
    for list_of_media in file_content:
        directors = list_of_media[3]
        directors_set.append(directors)
    return set(directors_set)


# print(get_directors(load_csv_file("netflix_titles.csv")))


def amount_tv_shows():
    return len((search_by_type(load_csv_file("netflix_titles.csv"), "TV Show")))


def amount_movies():
    return len((search_by_type(load_csv_file("netflix_titles.csv"), "Movie")))


def directors_tv_shows_movies():
    netflix_titles = load_csv_file("netflix_titles.csv")
    set_directors = get_directors(netflix_titles)
    list_of_directors_plus_works = []
    list_of_directors = []
    for director in set_directors:
        list_of_shows = search_by_director(netflix_titles, director)
        list_of_directors_plus_works.append((director, list_of_shows))
    for director, movies in list_of_directors_plus_works:
        movie = False
        tv_show = False
        for film in movies:
            if film[1] == "Movie":
                movie = True
            if film[1] == "TV Show":
                tv_show = True
        if movie and tv_show:
            list_of_directors.append(director)
    list_of_directors.remove("")
    return sorted(list_of_directors)


def director_work_count():
    netflix_titles = load_csv_file("netflix_titles.csv")
    set_directors = get_directors(netflix_titles)
    list_of_directors_plus_works = []
    list_of_directors = []
    for director in set_directors:
        list_of_shows = search_by_director(netflix_titles, director)
        list_of_directors_plus_works.append((director, list_of_shows))
    for director, movies in list_of_directors_plus_works:
        movie = 0
        tv_show = 0
        for film in movies:
            if film[1] == "Movie":
                movie += 1
            if film[1] == "TV Show":
                tv_show += 1
        list_of_directors.append((director, movie, tv_show))
    return sorted(list_of_directors)


def main():
    print("[1] Print the amount of TV Shows")
    print("[2] Print the amount of Movies")
    print(
        "[3] Print the names of directors in alphabetical order whom directed both tv shows and movies."
    )
    print(
        "[4] Print the name of each director in alphetical order, number of movies and the number of tv they directed"
    )
    user_menu_choice = input("Enter the corresponding number: ")
    if user_menu_choice == "1":
        print(amount_tv_shows())
    elif user_menu_choice == "2":
        print(amount_movies())
    elif user_menu_choice == "3":
        print(directors_tv_shows_movies())
    elif user_menu_choice == "4":
        print(director_work_count())


if __name__ == "__main__":
    main()
