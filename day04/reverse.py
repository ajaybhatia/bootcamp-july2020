# Write a script in python to print a number in reverse of a number

num = int(input("Enter any number: "))

while num > 0:
    digit = num % 10
    print(digit, end="")
    num //= 10

print()
