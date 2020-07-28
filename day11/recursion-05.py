'''
Fibonacci sequence
1  2  3  4  5  6
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, .........

f(1) = 1
f(2) = 1
f(n) = f(n-1) + f(n-2)

f(6) = f(5) + f(4)
     = f(4) + f(3) + f(3) + f(2)
     = f(3) + f(2) + f(2) + f(1) + f(2) + f(1) + f(2)
     = f(3) + 1 + 1 + 1 + 1 + 1 + 1
     = f(3) + 6
     = 1 + 1 + 6 = 8
'''


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_seq(limit, step=1):
    if step == limit:
        print(fib(step))
        return
    else:
        print(fib(step), end=" ")
        return fib_seq(limit, step+1)


fib_seq(5)


# for i in range(1, 11):
#     print(fib(i))
