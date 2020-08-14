# import numpy before using it
import numpy as np

a = np.arange(15).reshape(3, 5)

# from numpy import arange, reshape

# a = arange(15).reshape(3, 5)

# Display numpy array
print(a)

# Display shape
print(a.shape)

# Display number of dimensions
print(a.ndim)

# Display datatype of values in numpy array
print(a.dtype.name)

# Type of numpy array
print(type(a))

# Total size of numpy array
print(a.size)
