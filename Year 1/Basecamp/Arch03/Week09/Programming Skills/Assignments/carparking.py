from datetime import datetime
import math


class CarParkingMachine:
    def __init__(self, capacity=10, hourly_rate=2.50, parked_cars={}):
        self.capacity = int(capacity)
        self.hourly_rate = float(hourly_rate)
        self.parked_cars = parked_cars

    def check_in(self, license_plate, check_in=datetime.now()):
        if len(self.parked_cars) >= self.capacity:
            return False
        else:
            self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
            return True

    def check_out(self, license_plate):
        if license_plate in self.parked_cars:
            parking_fee = self.get_parking_fee(license_plate)
            self.parked_cars.pop(license_plate)
            return parking_fee
        else:
            return 0.0

    def get_parking_fee(self, license_plate):
        if license_plate in self.parked_cars:
            current_time = datetime.now()
            # one_hour_extra = self.parked_cars[license_plate].check_in + timedelta(hours=1)
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


def main():
    parking_lot = CarParkingMachine()
    while True:
        print("[I] Check-in car by license plate")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")
        user_choice = input("Enter your choice: ").lower()
        if user_choice == "i":
            license_plate = input("Enter license plate: ")
            if license_plate not in parking_lot.parked_cars:
                parking_lot.check_in(license_plate)
                if parking_lot.check_in(license_plate) is True:
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
