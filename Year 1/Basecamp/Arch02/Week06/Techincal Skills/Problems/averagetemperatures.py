temperatures = (
    ('1995', '3',
     ['47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1',
      '40.5', '41.6', '43.2', '46.2', '45.8', '44.9', '39.4', '40.5',
      '42.0', '46.5', '46.2', '43.3', '41.7', '40.7', '39.6', '44.2', '47.8', '45.9',
      '47.3', '39.8', '35.2', '38.5', '40.5', '47.0']),
    ('2010', '3',
     ['39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2',
      '32.3', '33.3', '37.3', '39.9', '40.8', '42.9', '42.7',
      '42.6', '44.8', '50.3', '52.2', '55.2', '47.2', '45.0', '48.6', '55.0',
      '57.4', '50.9', '48.6', '46.2', '49.6', '50.1', '43.6']),
    ('2020', '3',
     ['43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0',
      '47.9', '46.6', '50.5', '51.5', '47.7', '44.7', '44.0', '48.9',
      '45.3', '46.6', '49.7', '47.2', '44.8', '41.8', '40.9', '41.0', '42.7',
      '43.4', '44.0', '46.4', '45.5', '40.7', '39.5', '40.6'])
)

"""
How many different values occur as a daily average temperature in both March 1995 and March 2010.
How many different values occur as a daily average temperature in both March 1995 and March 2020.
Which year has a day with highest temperature in March?
Which year had the warmest March?
"""
# Here I unpack the tuple into each year, giving me a 3 new tuples
year_1995, year_2010, year_2020 = temperatures

# Here I eliminate the year and month digits, saving only the temps
temp_1995 = []
for temperature in year_1995[2]:
    temperature = float(temperature)
    temp_1995.append(temperature)


temp_2010 = []
for temperature in year_2010[2]:
    temperature = float(temperature)
    temp_2010.append(temperature)


temp_2020 = []
for temperature in year_2020[2]:
    temperature = float(temperature)
    temp_2020.append(temperature)


def first_question():
    set_1995 = set(temp_1995)
    set_2010 = set(temp_2010)
    set_together = set_1995.intersection(set_2010)
    answer_one = len(set_together)
    print(answer_one)


def second_question():
    set_1995 = set(temp_1995)
    set_2020 = set(temp_2020)
    set_together = set_1995.intersection(set_2020)
    answer_two = len(set_together)
    print(answer_two)


def third_question():
    highest_1995 = max(temp_1995)
    highest_2010 = max(temp_2010)
    highest_2020 = max(temp_2020)
    if highest_1995 > highest_2010:
        if highest_1995 > highest_2020:
            print("1995")
        else:
            print("2020")
    else:
        if highest_2010 > highest_2020:
            print("2010")
        else:
            print("2020")
    ...


def fourth_question():
    total_1995 = sum(map(float, temp_1995))
    total_2010 = sum(map(float, temp_2010))
    total_2020 = sum(map(float, temp_2020))
    if total_1995 > total_2010:
        if total_1995 > total_2020:
            print("1995")
        else:
            print("2020")
    else:
        if total_2010 > total_2020:
            print("2010")
        else:
            print("2020")
    ...


if __name__ == "__main__":
    first_question()
    second_question()
    third_question()
    fourth_question()
    ...
