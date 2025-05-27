import os
import sys
import json
import sqlite3
from datetime import datetime, timedelta


def default_menu():
    print("""
[B] Borrow book
[R] Return book
[S] Search book
[Q] Quit program
    """)


def json_to_database():
    con = sqlite3.connect(os.path.join(sys.path[0], 'bookstore.db'))
    books_in_database = """
    SELECT isbn FROM books
    """
    # list comprehension to add all isbn numbers in a list
    all_isbns = [isbn[0] for isbn in con.execute(books_in_database).fetchall()]
    update_books = """
    INSERT INTO books (isbn, title, author, pages, year) VALUES (?, ?, ?, ?, ?)
    """
    with open(os.path.join(sys.path[0], 'books.json'), 'r') as f:
        books = json.load(f)
        print(all_isbns)
        for book in books:
            # if the isbn is not in the list, the book is added to the database
            if book['isbn'] not in all_isbns:
                con.execute(update_books, [book['isbn'], book['title'],
                                           book['author'], book['pages'], book['year']])
    con.commit()
    con.close()


def main():
    con = sqlite3.connect(os.path.join(sys.path[0], 'bookstore.db'))
    con = con.cursor()
    con.execute(
        '''CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            pages INTEGER NOT NULL,
            year TEXT NOT NULL,
            status TEXT DEFAULT "AVAILABLE",
            return_date DATE DEFAULT NULL
        );'''
    )
    con = con.execute("SELECT * FROM books")
    in_database = con.fetchall()

    with open(os.path.join(sys.path[0], 'books.json'), 'r') as f:
        books = json.load(f)
        if len(books) != len(in_database):
            json_to_database()
        else:
            pass

    def borrow_book():
        con = sqlite3.connect(os.path.join(sys.path[0], 'bookstore.db'))
        book_id = input("Enter book ID or ISBN: ")
        duration = input("Enter borrow duration: ")

        # Is the book available
        is_book_available = """
        SELECT * FROM books WHERE id = ? and status = 'AVAILABLE' or isbn = ? and status = 'AVAILABLE'
        """
        get_book_values = con.execute(is_book_available, [book_id, book_id])
        book_values = get_book_values.fetchall()
        print(len(book_values))

        change_to_borrowed = """
        UPDATE books
        SET status = 'BORROWED',
            return_date = ?
        WHERE id = ? or isbn = ?
        """

        if len(book_values) > 0:
            return_date = (datetime.now() + timedelta(days=int(duration))).strftime("%d-%m-%Y")
            con.execute(change_to_borrowed, (return_date, book_id, book_id))
            con.commit()
            print(f"Borrowed {book_id} at {datetime.now().strftime('%m/%d/%Y')} should be return on {return_date}")
        else:
            print("Book not found")
        con.close()

    def return_book():
        # I get book ID, check if book has been borrowed
        con = sqlite3.connect(os.path.join(sys.path[0], 'bookstore.db'))
        book_id = input("Enter book ID or ISBN: ")
        get_return_book = """
        SELECT * FROM books
        WHERE id = ? and status = 'BORROWED'
        or isbn = ? and status = 'BORROWED'
        """

        book_loaned = con.execute(get_return_book, [book_id, book_id]).fetchone()

        book_back_in_shelf = """
        UPDATE books
        SET status = 'AVAILABLE',
            return_date = NULL
        WHERE id = ? and status = 'BORROWED'
        or isbn = ? and status = 'BORROWED'
        """
        try:
            date_of_return = book_loaned[-1]
            date_of_return_object = datetime.strptime(date_of_return, '%d-%m-%Y')
            real_date_of_return = datetime.now()
            if real_date_of_return > date_of_return_object:
                days_missed = str(real_date_of_return - date_of_return_object).split(" ")
                price = float(days_missed[0]) * 0.5
                if book_loaned is not None:
                    con.execute(book_back_in_shelf, [book_id, book_id])
                    print(f"The book: {book_loaned} has been returned successfully.\n"
                          f"Being late fee: {price:.2f}")
                    con.commit()
                else:
                    print("Book not found")
            else:
                con.execute(book_back_in_shelf, [book_id, book_id])
                print("Thank you for bringing it back on time!")

        except TypeError:
            print("Book not found")
        con.commit()
        con.close()

    def search_book():
        con = sqlite3.connect(os.path.join(sys.path[0], 'bookstore.db'))
        book_id = input("Enter book ID or ISBN: ")
        book_query = """
        SELECT * FROM books WHERE id = ? or isbn = ?
        """
        book_loaned = con.execute(book_query, [book_id, book_id]).fetchone()
        info_dict = {"id": book_loaned[0], "isbn": book_loaned[1],
                     "title": book_loaned[2], "author": book_loaned[3],
                     "pages": book_loaned[4], "year": book_loaned[5],
                     "status": book_loaned[6], "return_date": book_loaned[7]}
        print(info_dict)
        con.close()

    while True:
        default_menu()
        user_input = input("> ").lower()
        if user_input == "b":
            borrow_book()
        elif user_input == "r":
            return_book()
        elif user_input == "s":
            search_book()
        elif user_input == "q":
            con.close()
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
