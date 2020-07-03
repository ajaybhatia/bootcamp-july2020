# First program/script to swap two numbers in python

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("Before swapping....")
print(f"a = {a}, b = {b}")

a, b = b, a

print("After swapping....")
print(f"a = {a}, b = {b}")
