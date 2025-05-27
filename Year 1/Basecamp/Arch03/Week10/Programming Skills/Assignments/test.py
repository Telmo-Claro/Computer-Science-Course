from datetime import datetime
import math

parked_car = {}

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
                        parked_car[license_plate] = check_in
                    if item == "action=check-out":
                        if license_plate in parked_car:
                            parked_car.pop(license_plate)
except IndexError:
    print("No cars logged.")
