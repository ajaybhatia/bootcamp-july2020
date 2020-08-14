# numpy operations
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[9, 12.4], [10, 1.2]])


print(a)
print(b)

Addition of numpy arrays
c = a + b
print(c)

Subtraction
c = a - b
print(c)

Multiplication
c = a * b
print(c)

Product
c = a @ b
print(c)

Division
c = a / 2
print(c)

Exponentation
c = a ** 2
print(c)

c = np.array([[10, 1, 5],
              [11, 2, 3],
              [67, 31, 89]]
             )

print(c.sum())
print(c.min())
print(c.max())
print(c.cumsum(axis=1))
print(c.cumprod(axis=0))
print(c.mean())
print(c.std())

c = np.array([90, 34, 78, 12, 41, 28, 67])
print(c[4])
print(c[-2])
print(c[0:5:2])

d = np.array([
    [10,  5,  9],
    [34, 11, 10],
    [45, 67, 99]
])

print(d[1, 1])
print(d[1:, 1:])

for row in d:
    print(row)

print(d.flatten(order='F'))
