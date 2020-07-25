'''
Sum of first n even numbers

5 = 10 + 8 + 6 + 4 + 2
5 = 10 + f(4)
5 = 10 + 8 + f(3)

f(1) = 2, B.C.
f(n) = 2*n + f(n-1)
'''


def sumeven(n):
    if n == 1:
        return 2
    else:
        return 2*n + sumeven(n-1)


print(sumeven(3))
