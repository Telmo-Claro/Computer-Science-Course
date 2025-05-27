from datetime import datetime
import math


class CarParkingMachine:
    def __init__(self, id, capacity=10, hourly_rate=2.50, parked_cars={}):
        self.capacity = int(capacity)
        self.hourly_rate = float(hourly_rate)
        self.parked_cars = parked_cars
        self.id = id
        self.car_parking_logger = CarParkingLogger(id)
        try:
            with open("carparklog.txt", "r") as file:
                for lines in file.readlines():
                    for line in lines.splitlines():
                        line = line.split(";")
                        for item in line:
                            item = item.strip()
                            license_plate = line[2][len("license_plate="):]
                            check_in = datetime.strptime(line[0], "%Y-%m-%d %H:%M:%S")
                            if item == "action=check-in":
                                self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
                            if item == "action=check-out":
                                if license_plate in self.parked_cars:
                                    self.parked_cars.pop(license_plate)
        except IndexError:
            print("No cars logged.")

    def check_in(self, license_plate, check_in=datetime.now()):
        check_in = check_in.replace(microsecond=0)
        if len(self.parked_cars) >= self.capacity:
            return False
        else:
            self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
            self.car_parking_logger.log_check_in(license_plate, check_in)
            print(self.parked_cars)
            return True

    def check_out(self, license_plate):
        if license_plate in self.parked_cars:
            parking_fee = self.get_parking_fee(license_plate)
            self.parked_cars.pop(license_plate)
            self.car_parking_logger.log_check_out(license_plate, parking_fee)
            return parking_fee
        else:
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
    def __init__(self, license_plate, check_in):
        self.license_plate = license_plate
        self.check_in = check_in


class CarParkingLogger:
    def __init__(self, id):
        self.id = id

    def log_check_in(self, license_plate, check_in):
        with open("carparklog.txt", "a") as file:
            file.write(f"{check_in};cpm_name={self.id};license_plate={license_plate};action=check-in \n")

    def log_check_out(self, license_plate, total_fee):
        current_time = datetime.now()
        current_time = current_time.replace(microsecond=0)
        with open("carparklog.txt", "a") as file:
            file.write(
                f"""{current_time};cpm_name={self.id};license_plate={license_plate};action=check-out;parking_fee={total_fee} \n"""
            )

    def get_machine_fee_by_day(self, car_parking_machine_id, search_date):
        with open("carparklog.txt", "r") as file:
            total_daily_fee = 0
            for lines in file.readlines():
                for line in lines.splitlines():
                    line = line.split(";")
                    if (
                        f"cpm_name={car_parking_machine_id}" in line[1]
                        and search_date in line[0]
                        and "action=check-out" in line[3]
                    ):
                        parking_fee = line[-1]
                        parking_fee = parking_fee.split("=")[-1]
                        parking_fee = float(parking_fee)
                        total_daily_fee += parking_fee
            total_daily_fee = math.ceil(total_daily_fee)
            return total_daily_fee

    def get_total_car_fee(self, license_plate):
        with open("carparklog.txt", "r") as file:
            car_total_fee = 0
            for lines in file.readlines():
                for line in lines.splitlines():
                    line = line.split(";")
                    if (
                        f"license_plate={license_plate}" in line[2]
                        and "action=check-out" in line[3]
                    ):
                        parking_fee = line[-1]
                        parking_fee = float(parking_fee.split("=")[-1])
                        car_total_fee += parking_fee
            return car_total_fee


def main():
    parking_lot = CarParkingMachine("North Side")
    while True:
        print("[I] Check-in car by license plate")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")
        user_choice = input("Enter your choice: ").lower()
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


if __name__ == "__main__":
    main()
