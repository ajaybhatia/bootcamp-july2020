'''
To find Greatest Common Divisor of two numbers
'''

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
