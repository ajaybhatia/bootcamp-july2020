# Write a script in python to find whether the number is palindrome or not

# 123

# 3X10**len-1 + 2X10**len-2 + 1X10**len-3

num = int(input("Enter any number: "))

temp, reverse, size, i = num, 0, len(str(num)), 1

while temp > 0:
    digit = temp % 10
    reverse += digit * (10**(size-i))
    temp //= 10
    i += 1

if num == reverse:
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")
