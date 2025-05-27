import os
import sys

"""
From template, reads the .txt file with the temperatures
"""


def load_txt_file(file_name):
    file_content = []
    with open(
        os.path.join(sys.path[0], file_name), newline="", encoding="utf8"
    ) as file_obj:
        for line in file_obj.readlines():
            file_content.append(line.split())
    return file_content


"""
Variables, self explanatory
"""

daily_temperatures_list = load_txt_file("NLAMSTDM.txt")

"""
To storage the data
"""


def sort_list(daily_temperatures_list):
    organized_temps = {}
    # unpacks each item in the list (mont, day, year and temps)
    for item in daily_temperatures_list:
        month, day, year, temp = item
        # adds the year to the list of dictionaries
        if year not in organized_temps:
            organized_temps[year] = {}
        # adds the month after the year
        if month not in organized_temps[year]:
            organized_temps[year][month] = []
        organized_temps[year][month].append(temp)  # Appends all temps
    return organized_temps


sorted_dictionary = sort_list(daily_temperatures_list)  # It works!

"""
This returns:
{2000': {'1': ['43.5', '44.9', '47.6', '42.8', '40.3', '44.8', '42.4',
'42.9', '37.6', '35.1', '38.0', '33.9', '34.5', '38.1', '37.8', '42.2',
'44.3', '44.3', '40.1', '42.1', '42.7', '41.3', '35.7', '29.5', '34.6',
'39.0', '39.9', '41.2', '47.8', '47.7', '48.3'],
'2': ['48.0', '45.5', '43.9', '45.1', '46.9', '45.4', '46.1', '47.4',
'44.1', '43.3', '41.5', '41.1', '42.7', '40.2', '43.5', '39.3', '40.1',
'41.3', '41.4', '37.6', '37.1', '39.5', '40.0', '45.9', '42.1', '40.2',
'46.0', '48.3', '44.0']}}
"""


def fahrenheit_to_celsius(fahrenheit: float) -> float:  # Tested, it works
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


"""
Create a function average_temp_per_month(temperatures_per_year: dict) -> list
that calculates the average temperature per month.
Return a list of tuples (month, temperature).
"""


# Ok I really hope this is what they want from me, I spent 2 hours just here, I want to shoot someone.
def average_temp_per_month(temperatures_per_year: dict) -> list:
    list_of_avg_temps_per_month = []
    for year, month_dict in temperatures_per_year.items():
        for month, temperatures_list in month_dict.items():
            month_total = 0
            for temperature in temperatures_list:
                month_total += float(temperature)
            month_avg = month_total / len(temperatures_list)
            list_of_avg_temps_per_month.append((int(month), month_avg))
    return list_of_avg_temps_per_month


average_month = average_temp_per_month(sorted_dictionary)


def average_temp_per_year(temperatures: dict) -> list:
    years = []
    average_yearly_temperatures = []
    final_list = []
    for year in temperatures:
        years.append(int(year))
    for months in temperatures.values():
        temp_count = 0
        day_count = 0
        for temp_list in months.values():
            for temp in temp_list:
                temp_count += float(temp)
            day_count += len(temp_list)
        average_yearly = temp_count / day_count
        average_yearly_temperatures.append(average_yearly)
        final_list = list(zip(years, average_yearly_temperatures))
    return final_list


average_year = average_temp_per_year(sorted_dictionary)


def average_temp_fahrenheit():
    yearly = average_temp_per_year(sorted_dictionary)
    list_of_averages = []
    for year_count in yearly:
        list_of_averages.append(year_count)
    return list_of_averages


def average_temp_celsius():
    yearly = average_temp_per_year(sorted_dictionary)
    list_of_averages = map(
        lambda year_count: (year_count[0], fahrenheit_to_celsius(year_count[1])), yearly
    )
    return list(list_of_averages)


# Sorted by the index[1], get both ends.
def warmest_and_coldest():
    yearly = average_temp_per_year(sorted_dictionary)
    yearly = sorted(yearly, key=lambda year: year[1])
    highest_temp = yearly[-1]
    lowest_temp = yearly[0]
    return (highest_temp[0], lowest_temp[0])


def warmest_of_year():
    user_year_input = int(input("Choose a year: "))
    months_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    year_monthly_average = {}
    for year, month_dict in sorted_dictionary.items():
        list_of_avg_temps_per_month = []
        for month, temps_list in month_dict.items():
            month_total = 0
            for temp in temps_list:
                month_total += float(temp)
            month_avg = month_total / len(temps_list)
            list_of_avg_temps_per_month.append((int(month), month_avg))
        year_monthly_average[int(year)] = list_of_avg_temps_per_month

    for years, items in year_monthly_average.items():
        if years == user_year_input:
            lowest_temperature = max(items, key=lambda x: x[1])
            print(lowest_temperature)
            month_max, temperature_max = lowest_temperature
            for month_number, month_name in months_dict.items():
                if month_number == month_max:
                    return months_dict.get(month_number)


def coldest_of_year():
    user_year_input = int(input("Choose a year: "))
    months_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    year_monthly_average = {}
    for year, month_dict in sorted_dictionary.items():
        list_of_avg_temps_per_month = []
        for month, temps_list in month_dict.items():
            month_total = 0
            for temp in temps_list:
                month_total += float(temp)
            month_avg = month_total / len(temps_list)
            list_of_avg_temps_per_month.append((int(month), month_avg))
        year_monthly_average[int(year)] = list_of_avg_temps_per_month

    for years, items in year_monthly_average.items():
        if years == user_year_input:
            lowest_temperature = min(items, key=lambda x: x[1])
            month_min, temperature_max = lowest_temperature
            for month_number, month_name in months_dict.items():
                if month_number == month_min:
                    return months_dict.get(month_number)


def WTF():
    future_tuple = []
    for year, month_dict in sorted_dictionary.items():
        list_of_avg_temps_per_month = []
        for month, temps_list in month_dict.items():
            month_total = 0
            for temp in temps_list:
                temp = fahrenheit_to_celsius(float(temp))
                month_total += temp
            month_avg = month_total / len(temps_list)
            list_of_avg_temps_per_month.append((int(month), float(month_avg)))
        future_tuple.append((int(year), dict(list_of_avg_temps_per_month)))
    return future_tuple


if __name__ == "__main__":
    choice = input("Input: ")
    if choice == "1":
        print(average_temp_fahrenheit())
    elif choice == "2":
        print(average_temp_celsius())
    elif choice == "3":
        print(warmest_and_coldest())
    elif choice == "4":
        print(warmest_of_year())
    elif choice == "5":
        print(coldest_of_year())
    elif choice == "6":
        print(WTF())
