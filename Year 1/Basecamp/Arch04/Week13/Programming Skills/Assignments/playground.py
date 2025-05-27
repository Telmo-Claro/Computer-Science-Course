import csv
from datetime import datetime
import sqlite3

conn = sqlite3.connect('carparkingmachine.db')
c = conn.cursor()
user_input = "TEST_JUAN"
find_car_query = """
SELECT * FROM parkings WHERE license_plate = ?
"""
fetched = c.execute(find_car_query, [user_input]).fetchall()

csv_path = f"all_parkings_for_{user_input}.csv"

with open(csv_path, "w") as csv_write:
    fieldnames = ["car_parking_machine", "check_in", "check_out", "total_parking_fee"]
    csv_writer = csv.DictWriter(csv_write, fieldnames=fieldnames, delimiter=";")
    csv_writer.writeheader()
    for row in fetched:
        csv_writer.writerow({"car_parking_machine": row[1],
                             "check_in": row[3],
                             "check_out": row[4],
                             "total_parking_fee": row[-1]})
