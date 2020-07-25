'''
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# Using Brute Force

# def is_divisible_1_through_20(n):
#     for i in range(1, 21):
#         if n % i != 0:
#             return False
#     return True


# num, i = 20, 2
# while True:
#     if (is_divisible_1_through_20(num)):
#         print(num)
#         break
#     num = 20 * i
#     i += 1


# Using LCM approach (User defined functions)

# def gcd(x, y):
#     while y != 0:
#         x, y = y, x % y
#     return x


# def lcm(x, y):
#     return x*y//gcd(x, y)


# result = 1
# for i in range(1, 51):
#     result = lcm(result, i)

# print(result)

# Using LCM approach (Built-in functions)
from math import gcd
from functools import reduce


def lcm(x, y): return x*y//gcd(x, y)


print(reduce(lcm, range(1, 11)))
