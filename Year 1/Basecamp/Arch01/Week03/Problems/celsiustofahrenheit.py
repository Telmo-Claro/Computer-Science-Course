# Celsius to Fahrenheit formula °F = (°C x 1.8) + 32

celsius = 0


def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return int(fahrenheit)


x = 0
print("°C °F")
while x <= 100:
    print(celsius, end=" ")
    fahrenheit = convert(celsius)
    print(fahrenheit)
    x += 10
    celsius += 10
