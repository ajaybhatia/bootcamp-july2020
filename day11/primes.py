# Prime numbers are divisible by 1 and itself
# Ourtest would be to check whether a number is divisible by 2 to n-1, for n

def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


print(is_prime(33))
