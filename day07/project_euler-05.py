'''
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def is_divisible_1_through_20(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True


num, i = 20, 2
while True:
    if (is_divisible_1_through_20(num)):
        print(num)
        break
    num = 20 * i
    i += 1
