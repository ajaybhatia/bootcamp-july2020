numbers = {1, 2, 3, 4, 3, 2, 5}
print(numbers)

numbers.add(9)
print(numbers)

numbers.discard(4)
print(numbers)

# numbers.remove(10)
# print(numbers)

a = {1, 2, 3, 4}
b = {3, 4, 5}
# Operations

# Intersection
print(a & b)

# Union
print(a | b)

# Difference
print(a - b)

# Symmetric Difference
print(a ^ b)

# Super set
print(a >= b)
print(a <= b)

# Deep copy
c = a.copy()
print(c is a)
