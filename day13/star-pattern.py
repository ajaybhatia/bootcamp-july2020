def show_stars1(rows):
    for row in range(1, rows+1):
        for col in range(1, row+1):
            print("*", end=" ")
        print()


def show_stars2(rows):
    for row in range(1, rows+1):
        for space in range(1, rows-row+1):
            print(" ", end=" ")
        for col in range(1, row+1):
            print("*", end=" ")
        print()


def show_stars3(rows):
    for row in range(1, rows+1):
        for space in range(1, rows-row+1):
            print(" ", end=" ")
        for col in range(1, 2*row):
            print("*", end=" ")
        print()


def show_stars4(rows):
    show_stars3(rows)
    for row in range(1, rows+1):
        for space in range(1, row+1):
            print(" ", end=" ")
        for col in range(1, 2*rows-(2*row-1)-1):
            print("*", end=" ")

        print()


show_stars4(12)
