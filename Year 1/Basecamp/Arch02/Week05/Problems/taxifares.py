def calculate_fare(distance):
    base_fare = 4.00
    price_per_140 = 0.25
    per_140 = 140
    distance = distance * 1000
    num_blocks = distance / per_140
    if num_blocks % 1 != 0:
        num_blocks = int(num_blocks) + 1
    total = base_fare + num_blocks * price_per_140
    total = round(total, 2)
    return total


if __name__ == "__main__":
    distance = float(input("Distance traveled: "))
    total_fare = calculate_fare(distance)
    print(f"Total fare: {total_fare:.2f} EUR")
