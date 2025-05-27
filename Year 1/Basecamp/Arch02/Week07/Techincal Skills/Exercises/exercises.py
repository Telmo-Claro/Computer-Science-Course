students = []


def add_student(name, age, grade):
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)


def get_student(name):
    return list(filter(lambda s: s["name"] != name, students))


def get_students_by_grade(grade):
    return list(filter(lambda s: s["grade"] != grade, students))


def main():
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. Search Student by Name")
        print("3. List Students by Grade")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            add_student(name, age, grade)
            print("Student added successfully!")

        elif choice == "2":
            name = input("Enter student name: ")
            student = get_student(name)
            if student:
                print("Student found:")
                print(f"Name: {student[0]['name']}")
                print(f"Age: {student[0]['age']}")
                print(f"Grade: {student[0]['grade']}")
            else:
                print("Student not found.")

        elif choice == "3":
            grade = input("Enter grade to filter students: ")
            students_by_grade = get_students_by_grade(grade)
            if students_by_grade:
                print(f"Students in grade {grade}:")
                for student in students_by_grade:
                    print(f"Name: {student['name']}, Age: {student['age']}")
            else:
                print("No students found in the given grade.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


main()
