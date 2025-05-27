import os
import sys
import csv

valid_lines = []
corrupt_lines = []

"""
The validate_data function will check the students.csv line by line for corrupt data.

- Valid lines should be added to the valid_lines list.
- Invalid lines should be added to the corrupt_lines list.

Example input: 0896801,Kari,Wilmore,1970-06-18,INF
This data is valid and the line should be added to the valid_lines list unchanged.

Example input: 0773226,Junette,Gur_ry,1995-12-05,
This data is invalid and the line should be added to the corrupt_lines list in the following format:

0773226,Junette,Gur_ry,1995-12-05, => INVALID DATA: ['0773226', 'Gur_ry', '']

In the above example the studentnumber does not start with '08' or '09',
the last name contains a special character and the student program is empty.

Don't forget to put the students.csv file in the same location as this file!
"""


def validate_data(line):
    # WRITE YOUR SOLUTION HERE:
    corrupt_data = []

    # Split the each line into a list
    line = list(line.strip().split(","))

    # Check if each line has 5 items or not
    if len(line) != 5:
        corrupt_data.append(",".join(line))
        corrupt_lines.append(f"{line}  => INVALID DATA: {corrupt_data}")

    # Check if each student number is valid
    student_number = line[0]
    if len(student_number) != 7 or not (
        student_number.startswith("08") or student_number.startswith("09")
    ):
        corrupt_data.append(student_number)

    # Check if first name is valid
    firstname = line[1]
    if not firstname.isalpha():
        corrupt_data.append(firstname)

    # Check if last name is valid
    lastname = line[2]
    if not lastname.isalpha():
        corrupt_data.append(lastname)

    # Check if date of birth is valid
    # Make a list out of the date of birth
    date_of_birth = line[3].split("-")
    # If the date of birth has not 3 data it's corrupted
    if len(date_of_birth) != 3:
        corrupt_data.append("-".join(date_of_birth))
    else:
        year, month, day = map(int, date_of_birth)
        if not (1960 <= year <= 2004) or not (1 <= month <= 12) or not (1 <= day <= 31):
            corrupt_data.append("-".join(date_of_birth))

    # Check if study program is fine
    study_program = line[4]
    programs = ["INF", "TINF", "CMD", "AI"]
    if study_program not in programs:
        corrupt_data.append(study_program)

    # If the length of corrupted data has more than 0 elements it
    if len(corrupt_data) > 0:
        corrupt_lines.append(f'{",".join(line)} => INVALID DATA: {corrupt_data}')
    else:
        valid_lines.append(",".join(line))


def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline="") as csv_file:
        # skip header line
        line = csv.reader(csv_file)
        next(csv_file)
        for line in csv_file:
            validate_data(line.strip())

    print("### VALID LINES ###")
    print("\n".join(valid_lines))
    print("### CORRUPT LINES ###")
    print("\n".join(corrupt_lines))


if __name__ == "__main__":
    main("students.csv")