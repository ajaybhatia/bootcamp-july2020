'''
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

num = 13195
for prime_factor in range(2, int(num**0.5)+1):
    if num % prime_factor == 0:
        num //= prime_factor
        print(prime_factor)

    if num == 1 or prime_factor == num:
        print(prime_factor)
        break
