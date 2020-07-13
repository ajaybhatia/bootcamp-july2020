'''
Largest palindrome product
Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

palindrome = 0

for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        prod = i * j
        s_prod = str(prod)
        if s_prod == s_prod[::-1]:
            if prod > palindrome:
                palindrome = prod

print(palindrome)
