'''
12345

1. Base Condition       : f(x) = x, if x < 10
2. Recursive Condition  : f(n) = n%10 and f(n//10)
'''


def reverse(n):
    if n < 10:
        print(n)
        return
    else:
        print(n % 10, end="")
        return reverse(n//10)


reverse(298312)
