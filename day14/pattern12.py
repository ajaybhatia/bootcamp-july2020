'''
      *
      *
      *
* * * * * * *
      *
      *
      *
'''

import sys


def is_even(n):
    return n % 2 == 0


def pattern(n):
    if is_even(n):
        n += 1
    for row in range(1, n):
        if row == n//2+1:
            for col in range(1, n+1):
                print("*", end=" ")
            print()
        for _ in range(1, n//2+1):
            print(" ", end=" ")
        print("*")


pattern(int(sys.argv[1]))
