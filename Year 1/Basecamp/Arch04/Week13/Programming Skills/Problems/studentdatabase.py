import os
import sys
import sqlite3


# make a student class so info is easily accessible
class Student:
    def __init__(self, first_name, last_name, city, date_of_birth, student_class=None):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.date_of_birth = date_of_birth
        self.student_class = student_class


# default option menu
def default_menu():
    print("[A] Add new student")
    print("[C] Assign student to class")
    print("[D] List all students")
    print("[L] List all students in class")
    print("[S] Search student")
    print("[Q] Quit program")


# Running everything from main()
def main():
    conn = sqlite3.connect(os.path.join(sys.path[0], 'studentdatabase.db'))
    cursor = conn.cursor()
    conn.execute(
        '''CREATE TABLE IF NOT EXISTS students (
            studentnumber INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            class TEXT DEFAULT NULL
        );'''
    )
    conn.commit()

    # This one works
    def add_student():
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        city = input("City: ")
        date_of_birth = input("Date of Birth: ")
        student_class = input("Class: ")
        new_student = Student(first_name,
                              last_name,
                              city,
                              date_of_birth,
                              student_class)

        # Get the last student number and give the next one using (MAX) value from Students table
        cursor.execute("SELECT MAX(studentnumber) FROM students")
        last_student_number = cursor.fetchone()[0]
        next_student_number = last_student_number + 1 if last_student_number else 1

        new_student_query = """
        INSERT INTO students (studentnumber, first_name, last_name, city, date_of_birth, class)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        conn.execute(new_student_query, (
            next_student_number,
            new_student.first_name,
            new_student.last_name,
            new_student.city,
            new_student.date_of_birth,
            new_student.student_class))
        conn.commit()
        print(next_student_number)
        conn.close()

    # Use fetch, if fetch is none, print message, else update.
    def assign_to_class():
        student_number = input("Student number: ")
        class_name = input("Class name: ")

        get_student = """
        SELECT * FROM students WHERE studentnumber = ?
        """
        res = conn.execute(get_student, (student_number,))
        if len(res.fetchall()) == 0:
            print(f"Could not find student with number: {student_number}")
        else:
            query_assign = """
            UPDATE students SET class = ? WHERE studentnumber = ?
            """
            conn.execute(query_assign, (class_name, student_number))
        conn.commit()
        conn.close()

    # Works
    def all_students():
        for row in cursor.execute("SELECT * FROM students ORDER BY class DESC"):
            print(row)
        conn.commit()
        conn.close()

    # Works
    def students_in_class():
        student_class = input("Class: ")
        for row in cursor.execute(f"SELECT * FROM students WHERE class = '{student_class}'"):
            print(row)
        conn.commit()
        conn.close()

    def search_student():
        search_term = input("Search term (first name, last name or city): ")
        query_search = """
        SELECT * FROM students WHERE city = ? OR first_name = ? OR last_name = ?
        """

        for row in conn.execute(query_search, [search_term, search_term, search_term]):
            print(row)
        conn.commit()
        conn.close()

    while True:
        default_menu()
        user_input = input("Menu choice: ").lower()
        if user_input == "a":
            add_student()
        if user_input == "c":
            assign_to_class()
        if user_input == "d":
            all_students()
        if user_input == "l":
            students_in_class()
        if user_input == "s":
            search_student()
        if user_input == "q":
            conn.close()
            break


if __name__ == "__main__":
    main()
