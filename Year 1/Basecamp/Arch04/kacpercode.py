from datetime import datetime
import os
import sys
import math


class ParkedCar:
    def __init__(self, license_plate, check_in):
        self.license = license_plate
        self.check_in = check_in


class CarParkingMachine:
    def __init__(self, id, capacity=10, hourly_rate=2.50, parked_cars={}):
        self.capacity = capacity
        self.actual_cp = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars
        self.id = id
        self.logger = CarParkingLogger(self.id)

        with open(os.path.join(sys.path[0], "carparklog.txt"), 'rt') as file:
            filedata = file.readlines()
        cardict = {}
        for line in filedata:
            linedata = line.split(";")
            time, id, license = datetime.strptime(linedata[0], r'%Y-%m-%d %H:%M:%S'), linedata[1][9:], linedata[2][14:]
            if license not in cardict.keys():
                cardict[license] = time
            elif license in cardict.keys():
                del cardict[license]
        for license_plate, time in cardict.items():
            self.parked_cars[license_plate] = ParkedCar(license_plate, time)

    def check_in(self, license_plate, check_in=None):
        if check_in is None:
            check_in = datetime.now().replace(microsecond=0)
        check_in = check_in.replace(microsecond=0)
        if self.actual_cp == 0:
            return False
        else:
            self.actual_cp -= 1
            self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
            self.logger.check_in_log(license_plate, check_in)
            return True

    def check_out(self, license_plate):
        if license_plate in self.parked_cars.keys():
            fee = self.get_parking_fee(license_plate)
            del self.parked_cars[license_plate]
            self.logger.check_out_log(license_plate, fee)
            return fee
        else:
            return False

    def get_parking_fee(self, license_plate):
        time = datetime.now() - self.parked_cars[license_plate].check_in
        time = math.ceil(time.total_seconds() / 3600)
        if time >= 24:
            return round(self.hourly_rate * 24, 2)
        else:
            return round(self.hourly_rate * time, 2)


class CarParkingLogger:
    def __init__(self, id):
        self.id = id

    def get_machine_fee_by_day(self, car_parking_machine_id, search_date):
        try:
            search_date = datetime.strptime(search_date, '%d-%m-%Y')
            search_date = search_date.strftime('%Y-%m-%d')
        except ValueError:
            pass
        with open(os.path.join(sys.path[0], "carparklog.txt"), 'rt') as file:
            filedata = file.readlines()
        fee = 0
        for line in filedata:
            line = line.split(";")
            if search_date == line[0][:10] and car_parking_machine_id == line[1][9:] and "parking_fee" == line[-1][:11]:
                fee += float(line[-1][12:])
        return round(fee, 2)

    def get_total_car_fee(self, license_plate):
        with open(os.path.join(sys.path[0], "carparklog.txt"), 'rt') as file:
            filedata = file.readlines()
        fee = 0
        for line in filedata:
            if f"{license_plate}" in line and "parking_fee=" in line:
                fee += float(line.split(";")[-1][12:])
        return fee

    def check_in_log(self, license_plate, date):
        with open(os.path.join(sys.path[0], "carparklog.txt"), 'at') as file:
            file.write(f"{date};cpm_name={self.id};license_plate={license_plate};action=check-in\n")

    def check_out_log(self, license_plate, fee):
        date = datetime.now().replace(microsecond=0)
        with open(os.path.join(sys.path[0], "carparklog.txt"), 'at') as file:
            file.write(f"{date};cpm_name={self.id};license_plate={license_plate};action=check-out;parking_fee={fee}\n")


def main():
    machine = CarParkingMachine("Pool")
    print(machine.id)
    print(machine.logger.get_machine_fee_by_day("Pool", "2024-04-10"))
    while True:
        print("[I] Check-in car by license plate\n"
              "[O] Check-out car by license plate\n"
              "[Q] Quit program")
        choice = input("Input: ").upper()

        if choice == "I":
            license_plate = input("License: ")
            if machine.actual_cp != 0:
                machine.check_in(license_plate)
                print("License registered")
                print(f"{machine.parked_cars.keys()}")
                print(machine.parked_cars[license_plate].check_in)
            else:
                print("Capacity reached!")

        if choice == "O":
            license_plate = input("License: ")
            if license_plate in machine.parked_cars.keys():
                print("Parking fee: %.2f EUR" % machine.check_out(license_plate))
                machine.check_out(license_plate)
                print(f"{machine.parked_cars.keys()}")
            else:
                print(f"License {license_plate} not found!")

        if choice == "Q":
            break


if __name__ == "__main__":
    main()
