'''
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from math import sqrt

num, primes, factors = 600851475143, [], []

# Generate a list of prime numbers
for i in range(2, num+1):
    isPrime = True  # Hypothesis
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)

# Factors of num
for i in primes:
    if num % i == 0:
        factors.append(i)

print(factors[-1])
