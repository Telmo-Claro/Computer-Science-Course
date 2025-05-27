temps = {"2000": {"1": ["10", "20", "15"],"2": ["5", "12", "14"]},
         "2001": {"1": ["7", "13", "14"],"2": ["2", "14", "20"]}}

new_list = []

def  average_temp_per_month(temperatures_per_year: dict) -> list:
    while True:
        year = temperatures_per_year.keys()
        if year in temperatures_per_year:
            for x in temperatures_per_year:
                if x not in new_list:
                    new_list.append(x)
            for i in temperatures_per_year.values():
                print(i)
                for a in i:
                    print(a)
            break
        else:
            print("Try again!")
    
    ...

average_temp_per_month(temps)

print(new_list)