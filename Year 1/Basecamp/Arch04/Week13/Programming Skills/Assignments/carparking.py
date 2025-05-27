import os
from datetime import datetime
import math
import sqlite3
import sys


class CarParkingMachine:
    def __init__(self, id, capacity=10, hourly_rate=2.50, parked_cars={}):
        self.id = id
        self.capacity = int(capacity)
        self.hourly_rate = float(hourly_rate)
        self.parked_cars = parked_cars

        # Makes table if it doesn't exist
        self.conn = sqlite3.connect('carparkingmachine.db')
        self.conn.execute(
            '''CREATE TABLE IF NOT EXISTS parkings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_parking_machine TEXT NOT NULL,
                license_plate TEXT NOT NULL,
                check_in TEXT NOT NULL,
                check_out TEXT DEFAULT NULL,
                parking_fee NUMERIC DEFAULT 0
            );'''
        )
        self.conn.commit()

        """
        This updates the parked_cars dictionary and makes an object of each car that are checked_in 
        and not yet checked_out.
        """
        get_parked_cars = '''
        SELECT * FROM parkings WHERE car_parking_machine=? and check_out is NULL
        '''
        parked_cars_con = self.conn.execute(get_parked_cars, [self.id]).fetchall()
        for car in parked_cars_con:
            id = car[0]  # Unpacking each car
            license_plate = car[2]
            check_in = car[3]
            check_in = datetime.strptime(check_in, "%Y-%m-%d %H:%M:%S")
            self.parked_cars[license_plate] = ParkedCar(id, license_plate, check_in)
        self.conn.commit()
        self.conn.close()

    # This method will search for a parked_car in the database base on the row ID and return a ParkedCar object with
    # the data
    def find_by_id(self, id):
        self.conn = sqlite3.connect(os.path.join(sys.path[0], 'carparkingmachine.db'))
        fetched_car = self.conn.execute("SELECT * FROM parkings WHERE id=?", [self.id]).fetchone()
        print(fetched_car)

    def check_in(self, license_plate, check_in=datetime.now()):
        self.conn = sqlite3.connect(os.path.join(sys.path[0], 'carparkingmachine.db'))

        check_in = check_in.replace(microsecond=0)

        if len(self.parked_cars) >= self.capacity:
            return False

        check_in_con = self.conn.execute("""
        SELECT * FROM parkings WHERE license_plate = ?
        """, [license_plate])
        fetched = check_in_con.fetchone()
        if fetched is None:
            self.conn.execute("""
            INSERT INTO parkings (car_parking_machine, license_plate, check_in) VALUES (?,?,?)
            """, [self.id, license_plate, check_in])
            self.conn.commit()
            self.conn.close()
            self.parked_cars[license_plate] = ParkedCar(self.id, license_plate, check_in, check_out=None, parking_fee=0)
            return True
        else:
            return False

    def check_out(self, license_plate):
        self.conn = sqlite3.connect(os.path.join(sys.path[0], 'carparkingmachine.db'))
        check_out = datetime.now()
        check_out = check_out.replace(microsecond=0)

        if license_plate in self.parked_cars:
            parking_fee = self.get_parking_fee(license_plate)
            self.parked_cars.pop(license_plate)

            self.conn.execute("""
            UPDATE parkings
            SET check_out = ?, parking_fee = ?
            WHERE license_plate = ?
            """, [check_out, parking_fee, license_plate])
            self.conn.commit()
            self.conn.close()

            return parking_fee

        self.conn.commit()
        self.conn.close()
        return 0.0

    def get_parking_fee(self, license_plate):
        if license_plate in self.parked_cars:
            current_time = datetime.now()
            time_difference = current_time - self.parked_cars[license_plate].check_in
            duration_in_hours = time_difference.total_seconds() / 3600
            duration_in_hours = math.ceil(duration_in_hours)
            if duration_in_hours >= 24:
                self.total_fee = 24 * self.hourly_rate
                self.total_fee = float(format(self.total_fee, ".2f"))
                return self.total_fee
            elif duration_in_hours <= 1:
                self.total_fee = self.hourly_rate
                self.total_fee = float(format(self.total_fee, ".2f"))
                return self.total_fee
            else:
                self.total_fee = duration_in_hours * self.hourly_rate
                self.total_fee = float(format(self.total_fee, ".2f"))
                return self.total_fee
        else:
            return 0.0


class ParkedCar:
    def __init__(self, id, license_plate, check_in, check_out=None, parking_fee=0):
        self.id = id
        self.license_plate = license_plate
        self.check_in = check_in
        self.check_out = check_out
        self.parking_fee = parking_fee


def main():
    parking_lot = CarParkingMachine("North")
    while True:
        print("[I] Check-in car by license plate")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")

        user_choice = input("> ").lower()

        if user_choice == "i":
            license_plate = input("Enter license plate: ")
            if license_plate not in parking_lot.parked_cars:
                if parking_lot.check_in(license_plate):
                    print("License registered!")
                else:
                    print("Capacity reached!")
            elif license_plate in parking_lot.parked_cars:
                print("License already in use!")

        if user_choice == "o":
            license_plate = input("Check out: ")
            if license_plate not in parking_lot.parked_cars:
                print("License not found!")
            else:
                parking_fee = format(parking_lot.check_out(license_plate), ".2f")
                print(f"Parking fee: {parking_fee} EUR")

        if user_choice == "q":
            break

        if user_choice == "m": # I use this to NUKE the whole table
            db_conn = sqlite3.connect(os.path.join(sys.path[0], 'carparkingmachine.db'))
            db_conn.execute("DROP TABLE IF EXISTS parkings")


if __name__ == "__main__":
    main()
