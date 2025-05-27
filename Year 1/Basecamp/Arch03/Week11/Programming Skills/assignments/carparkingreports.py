import csv
from datetime import datetime


def parking_information():
    user_input = input("Please enter machine ID, from date, to date: ")
    user_date = user_input.split(",")
    parking_machine_id = user_date[0]
    from_date = user_date[1]
    from_date_object = datetime.strptime(from_date, "%d-%m-%Y")
    from_date_string = from_date_object.strftime("%d-%m-%Y")
    to_date = user_date[2]
    to_date_object = datetime.strptime(to_date, "%d-%m-%Y")
    to_date_string = to_date_object.strftime("%d-%m-%Y")
    # class to str
    csv_file_path = f"parkedcars_{parking_machine_id}_from_{from_date_string}_to_{to_date_string}.csv"
    cars_dict_check_in = {}
    cars_dict_check_out = {}
    with open("carparklog.txt", "r") as file:
        for lines in file.readlines():
            for line in lines.splitlines():
                line = line.split(";")
                if len(line) <= 4:
                    check_in_date = line[0]
                    print(line)
                    date_time_object = datetime.strptime(check_in_date, "%d-%m-%Y %H:%M:%S")
                    machine_id = line[1].split("=")[1]
                    license_plate = line[2].split("=")[1]
                    check_in = line[3].split("=")[1]
                    if parking_machine_id == machine_id and from_date_object <= date_time_object <= to_date_object:
                        cars_dict_check_in[license_plate] = check_in_date
                if len(line) > 4:
                    check_out_date = line[0]
                    date_time_object = datetime.strptime(check_out_date, "%d-%m-%Y %H:%M:%S")
                    machine_id = line[1].split("=")[1]
                    license_plate = line[2].split("=")[1]
                    check_out = line[3].split("=")[1]
                    parking_fee = line[-1].split("=")[1]
                    if parking_machine_id == machine_id and from_date_object <= date_time_object <= to_date_object:
                        cars_dict_check_out[license_plate] = {check_out_date: parking_fee}
    csv_dump = []
    for checked_in_cars in cars_dict_check_in.items():
        checked_in_LP, checked_in_time = checked_in_cars
        for checked_out_cars in cars_dict_check_out.items():
            checked_out_LP, check_out_price = checked_out_cars
            if checked_in_LP == checked_out_LP:
                csv_dump.append([checked_in_LP, checked_in_time, check_out_price])
    
    with open(csv_file_path, "w") as csv_write:
        fieldnames = ["license_plate", "checked_in", "checked_out", "parking_fee"]
        csv_writer = csv.DictWriter(csv_write, fieldnames=fieldnames, delimiter=";")
        csv_writer.writeheader()
        for date in csv_dump:
            for item in date[2].items():
                csv_writer.writerow(
                    {"license_plate": date[0], "checked_in": date[1], "checked_out": item[0], "parking_fee": item[1]})


def parking_fee():
    user_input = input("Please enter from date, to date: ")
    user_date = user_input.split(",")
    from_date = user_date[0]
    from_date_object = datetime.strptime(from_date, "%d-%m-%Y")
    to_date = user_date[1]
    to_date_object = datetime.strptime(to_date, "%d-%m-%Y")
    csv_file_path = "total_fee.csv"
    cars_list_check_in = []
    cars_list_check_out = []

    with open("carparklog.txt", "r") as file:
        for lines in file.readlines():
            id_license = []
            for line in lines.splitlines():
                line = line.split(";")
                if len(line) <= 4:
                    check_in_date = line[0]
                    date_time_object = datetime.strptime(check_in_date, "%d-%m-%Y %H:%M:%S")
                    machine_id = line[1].split("=")[1]
                    license_plate = line[2].split("=")[1]
                    check_in = line[3].split("=")[1]
                    if from_date_object <= date_time_object <= to_date_object:
                        car_id = [machine_id, license_plate]
                        cars_list_check_in.append(car_id)

                if len(line) > 4:
                    check_out_date = line[0]
                    date_time_object = datetime.strptime(check_out_date, "%d-%m-%Y %H:%M:%S")
                    machine_id = line[1].split("=")[1]
                    license_plate = line[2].split("=")[1]
                    check_out = line[3].split("=")[1]
                    parking_fee = line[-1].split("=")[1]
                    if from_date_object <= date_time_object <= to_date_object:
                        car_id = [machine_id, license_plate, parking_fee]
                        cars_list_check_out.append(car_id)

    total_fees = []

    for car_in in cars_list_check_in:
        car_in_machine_id = car_in[0]
        car_in_license = car_in[1]
        fee_per_car = {car_in_machine_id: 0}
        for car_out in cars_list_check_out:
            car_out_machine_id = car_out[0]
            car_out_license = car_out[1]
            car_out_parking_fee = car_out[-1]
            if car_in_machine_id == car_out_machine_id and car_in_license == car_out_license:
                fee_per_car[car_in_machine_id] = fee_per_car[car_in_machine_id] + float(car_out_parking_fee)
        if not fee_per_car[car_in_machine_id] == 0:
            total_fees.append(fee_per_car)

    csv_dump = []
    car_parking_machine = ""
    total_fee = 0
    for item in total_fees:
        for id, fee in item.items():
            car_parking_machine = id
            total_fee += fee
    csv_dump.append([car_parking_machine, total_fee])

    with open(csv_file_path, "w") as csv_write:
        fieldnames = ["car_parking_machine", "total_parking_fee"]
        csv_writer = csv.DictWriter(csv_write, fieldnames=fieldnames, delimiter=";")
        csv_writer.writeheader()
        for items in csv_dump:
            csv_writer.writerow({"car_parking_machine": items[0], "total_parking_fee": items[1]})



def main():
    print("[P] Report all parked cars during a parking period for a specific parking machine")
    print("[F] Report total collected parking fee during a parking period for all parking machines")
    print("[Q] Quit program")
    menu_choice = input("Enter a letter: ").lower()
    if menu_choice == "p":
        parking_information()
    if menu_choice == "f":
        parking_fee()
    if menu_choice == "q":
        quit()


if __name__ == "__main__":
    main()
