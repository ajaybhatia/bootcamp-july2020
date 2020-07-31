import sys


def product(*arg):
    prod = 1
    for val in arg[0]:
        prod *= int(val)
    return prod


print(product(sys.argv[1:]))
