# Comparison/Relational Operators

# <, <=, >, >=, ==, !=

a = 5
b = 6

print(a < b)

# Logical Operators

# or, not, and

a = 5
b = 10
c = 8

print(a < b or a > c)
print(a < b and a > c)
print(not a < b)
print(True or False)
print(not False)

# Special Case
print(True + 1)  # 2
print(False * 2)  # 0
print(True - 1)  # 0

print(bool(10.67))  # True
print(bool(-18))  # True
print(bool(0))  # False


# Assignment Operators

# =, +=, -=, *=, /=, //=, %=, **=

a = 10
a **= 2
print(a)

# Bitwise Operators

# & (Bitwise AND)
# | (Bitwise OR)
# ^ (Bitwise XOR)
# ~ (Bitwise NOT)
# >> (Bitwise Right Shift)
# << (Bitwise Left Shift)

a = 15  # 1111
b = 9  # 1001

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a >> 1)  # a / 2**b
print(a << 2)  # a * 2**b

# Identity Operators
# is, is not

a = 10
b = 20
print(b is a)

# Membership Operators
# in, not in

a = [1, 3.13, 'apple', 3+9j, [1, 2, 3]]
print('banana' in a)
