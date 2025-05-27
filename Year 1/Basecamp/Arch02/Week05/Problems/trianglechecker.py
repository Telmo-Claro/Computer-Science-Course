def check_triangle(side_a, side_b, side_c) -> bool:
    return (
        side_a + side_b > side_c
        and side_a + side_c > side_b
        and side_b + side_c > side_a
    )


if __name__ == "__main__":
    side_a = int(input("Side A: "))
    side_b = int(input("Side B: "))
    side_c = int(input("Side C: "))
    triangle = check_triangle(side_a, side_b, side_c)
    if triangle:
        print("Possible triangle")
    else:
        print("Impossible triangle")
