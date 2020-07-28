'''
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

sum = 3000

for a in range(1, sum//3+1):
    for b in range(a, sum//2+1):
        c = sum - a - b
        if a**2 + b**2 == c**2:
            print(f"{a}, {b}, {c}")
            break
