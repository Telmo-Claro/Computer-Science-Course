# A empty list where the books (dictionary) are gonna be stored
list_books = []


# Function to add a book when called.
def add_book(**new_book):
    # Searches each dictionary in list_books
    for book_dictionary in list_books:
        # If titles fully match, it prints it already exists
        if new_book["title"] == book_dictionary["title"]:
            print("Book already added.")
            return

    # Just adds the book to the list
    list_books.append(new_book)
    print("Book has been added")
    print(list_books)


def search_book(books, term):
    for dictionaries in books:
        if term.lower() in dictionaries.values():
            return True
    return False


if __name__ == "__main__":
    # Prints the main menu
    print(
        """[A] Add book
[S] Search book
[E] Exit (and print)"""
    )

    while True:
        user_choice = input("Input: ")
        if user_choice.lower() == "a":
            new_book = input("Book details: ").strip().split(",")
            add_book(
                title=new_book[0],
                author=new_book[1],
                publisher=new_book[2],
                pub_date=new_book[3],
            )
        elif user_choice.lower() == "s":
            search_term = input("Search term: ").lower()
            found = search_book(list_books, search_term)
            if found:
                print(f"Found a book for: {search_term}")
            else:
                print("Book not found.")
        elif user_choice.lower() == "e":
            for dicky in list_books:
                print(dicky)
            break
        else:
            print("Input error")
