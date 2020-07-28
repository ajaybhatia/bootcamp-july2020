# def sum(a=10, b=1, c=2):
#     return a+b+c


# print(sum())


# def sum(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s


# print(sum(1, 2))


# def sum2(**kargs):
#     print(f"{kargs['name']} is {kargs['age']} years old.")


# def f(*args, **kargs):
#     print(args, kargs)


# f(1, 2, 3, a=10, b=20, c="apple")


# def swap(a, b):
#     return b, a


# print(swap(1, 2))

# l = (10, 20)
# a, b = l

# print(a, b)

# First class functions
# def x(n):
#     def y(m):
#         return n+m
#     return y


# a = x(10)
# b = a(20)
# print(b)


def square_series(n):
    for i in range(1, n+1):
        yield i**2


x = square_series(10)
for _ in range(1, 10):
    print(next(x))
