import sqlite3

"""
Conditions like AND and OR
Compare with =, >, >=, <, <=, <>, in

%x — will select all values that begin with x
%x% — will select all values that include x
x% — will select all values that end with x
x%y — will select all values that begin with x and end with y
_x% — will select all values have x as the second character
x_% — will select all values that begin with x and are at least two characters long. 
You can add additional _ characters to extend the length requirement, i.e. x___%

UPDATE

The UPDATE statement is used to update data in a table.
UPDATE customers
SET age = 56
WHERE name = ‘Bob’;

"""
school = sqlite3.connect("school.sqlite")
query = """
INSERT INTO students (name, date_of_birth, city, class)
VALUES (?,?,?,?)
"""
school.execute(query,["Telmo Claro", "2000-05-01", "Rotterdam", "F"])
school.commit()
