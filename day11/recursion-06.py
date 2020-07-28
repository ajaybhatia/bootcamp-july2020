'''
12345

1. Base Condition       : f(x) = x, if x < 10
2. Recursive Condition  : f(n) = n%10 and f(n//10)
'''


def reverse1(n):
    if n < 10:
        print(n)
        return
    else:
        print(n % 10, end="")
        return reverse1(n//10)


def reverse2(n, num=0):
    if n < 10:
        num += n
        return num
    else:
        num += (n % 10) * 10**(len(str(n))-1)
        return reverse2(n//10, num)


def palindrome(n):
    return n == reverse2(n)


print(palindrome(1221))

# reverse(298312)
