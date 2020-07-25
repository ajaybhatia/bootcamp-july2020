'''
A recursive function is a function which calls itself till some condition is met

For E.g
5! = 5 X 4 X 3 X 2 X 1
5! = 5 X 4!
   = 5 X 4 X 3!

f(1) = 1,          Base condition
f(n) = n * f(n-1), Recursive condition
'''

# Iterative Function


def factorial1(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result


# Recursive Function
def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n-1)


# print(factorial1(1000))
print(factorial2(1000))
