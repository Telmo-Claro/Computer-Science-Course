grades = [
    {"name": "Alice", "grade": 65},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 88},
]


def calculate_average_grade(grades):
    all_grades = 0
    num_students = len(grades)
    for x in grades:
        all_grades += x["grade"]
    finito = all_grades / len(grades)
    print(finito)


calculate_average_grade(grades)