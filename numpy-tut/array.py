# Numpy array

import numpy as np

# a = np.array([10., 1, 10])
# print(a)
# print(a.dtype.name)

b = np.array([(1, 2, 3), (4, 5, 6)])
print(b)

# Explicitly conversion
c = np.array([['1', 2], [3, 4]], dtype='float64')
print(c)
print(c.dtype.name)

# Zero filled numpy array
d = np.zeros((3, 3))
print(d)

# Ones filled numpy array
e = np.ones((3, 4), dtype='int64')
print(e)

# Empty numpy
f = np.empty((2, 5))
print(f)

# numpy identity array
g = np.identity(4)
print(g)

# linear spaced array
e = np.linspace(1.1, 2, 10)
print(e)
