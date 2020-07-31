'''
*       *
  *   *
    *
  *   *
*       *
'''
import sys


def pattern(n):
    if n % 2 == 0:
        n += 1
    for row in range(1, n+1):
        for col in range(1, n+1):
            if row == col or col == n-row+1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


pattern(int(sys.argv[1]))
