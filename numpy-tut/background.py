# Create a matrix using list

# 2X3 Matrix
a = [[1, 2, 3], [4, 5, 6]]

# 2X3 Matrix
b = [[4, 5, 6], [1, 2, 3]]

# Arithmetic Operations
c = []
for row in range(2):
    temp = []
    for col in range(3):
        temp.append(a[row][col] + b[row][col])
    c.append(temp)

print(c)
