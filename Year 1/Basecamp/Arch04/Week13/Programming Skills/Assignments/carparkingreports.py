import csv
from datetime import datetime
import sqlite3


def parking_information():
    conn = sqlite3.connect('carparkingmachine.db')
    user_input = input("Please enter parking machine, from date, to date:\n> ")
    user_data = user_input.split(",")
    parking_machine_id = user_data[0]
    from_date = user_data[1]
    to_date = user_data[2]

    from_date_object = datetime.strptime(from_date, "%d-%m-%Y")
    to_date_object = datetime.strptime(to_date, "%d-%m-%Y")

    db_get_id = conn.execute("""
        SELECT *
        FROM parkings 
        WHERE car_parking_machine = ?
        ORDER BY check_in DESC
    """, [parking_machine_id])

    conn.commit()
    db_rows = db_get_id.fetchall()
    csv_file_path = f"parkedcars_{parking_machine_id}_from_{from_date}_to_{to_date}.csv"

    with open(csv_file_path, "w") as csv_write:
        fieldnames = ["license_plate", "checked_in", "checked_out", "parking_fee"]
        csv_writer = csv.DictWriter(csv_write, fieldnames=fieldnames, delimiter=";")
        csv_writer.writeheader()
        for date in db_rows:
            if date[4] is None:
                pass
            else:
                csv_writer.writerow(
                    {"license_plate": date[2], "checked_in": date[3], "checked_out": date[4], "parking_fee": date[5]})

    conn.commit()
    conn.close()


def parking_fee():
    conn = sqlite3.connect('carparkingmachine.db')
    user_input = "20-05-2024,30-05-2024"
    user_date = user_input.split(",")
    from_date = user_date[0]
    to_date = user_date[1]
    csv_file_path = f"totalfee_from_{from_date}_to_{to_date}.csv"

    from_date_object = datetime.strptime(from_date, "%d-%m-%Y")
    to_date_object = datetime.strptime(to_date, "%d-%m-%Y")

    search_query = """
    SELECT *
    FROM parkings
    WHERE check_in >= ?
    """

    fetched = conn.execute(search_query, [from_date_object]).fetchall()

    with open(csv_file_path, "w") as csv_write:
        fieldnames = ["car_parking_machine", "total_parking_fee"]
        csv_writer = csv.DictWriter(csv_write, fieldnames=fieldnames, delimiter=";")
        csv_writer.writeheader()
        for row in fetched:
            if row[-1] == 0:
                pass
            else:
                print(row)
                csv_writer.writerow({"car_parking_machine": row[1], "total_parking_fee": row[-1]})
    conn.commit()
    conn.close()


def parking_specific_license():
    conn = sqlite3.connect('carparkingmachine.db')
    c = conn.cursor()
    user_input = input("License plate:\n> ")
    find_car_query = """
    SELECT * FROM parkings WHERE license_plate = ? ORDER BY check_in DESC
    """
    fetched = c.execute(find_car_query, [user_input]).fetchall()

    csv_path = f"all_parkings_for_{user_input}.csv"

    with open(csv_path, "w") as csv_write:
        fieldnames = ["car_parking_machine", "check_in", "check_out", "parking_fee"]
        csv_writer = csv.DictWriter(csv_write, fieldnames=fieldnames, delimiter=";")
        csv_writer.writeheader()
        for row in fetched:
            csv_writer.writerow({"car_parking_machine": row[1],
                                 "check_in": row[3],
                                 "check_out": row[4],
                                 "parking_fee": row[-1]})
    conn.commit()
    conn.close()


def main():
    print("[P] Report all parked cars during a parking period for a specific parking machine")
    print("[F] Report total collected parking fee during a parking period for all parking machines")
    print("[C] Report all complete parkings over all parking machines for a specific car")
    print("[Q] Quit program")
    menu_choice = input("> ").lower()
    if menu_choice == "p":
        parking_information()
    if menu_choice == "f":
        parking_fee()
    if menu_choice == "c":
        parking_specific_license()
    if menu_choice == "q":
        quit()


if __name__ == "__main__":
    main()
