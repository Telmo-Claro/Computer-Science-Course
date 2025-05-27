width = int(input("Width: "))
height = int(input("Height: "))

for y in range(height):
    for x in range(width):
        print((y*width+x) % 10, end=" ")
    print()
