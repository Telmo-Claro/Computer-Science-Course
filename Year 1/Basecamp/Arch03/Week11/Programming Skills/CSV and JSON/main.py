import csv
import json

"""
Open files with open().
With csv.read() and csv.write you can read and write csv files. (It is read as a list (of strings)).
Iterate through rows and process data.
"""

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

"""
csv.DictReader
Is a class used to read a csv file as dictionaries.
The keys are taken from the first row of the file.
"""

"""
JSON
Inspired by JavaScript.
Looks like a dictionary.
"""

"""
JSON.load() loads a json file as a dictionary.
Also open the file with open().
"""

with open("data.json", "r") as file:
    reader = json.load(file)
    # Extracting data
    print(reader["name"])
    print(reader["age"])
    print(reader["gender"])
