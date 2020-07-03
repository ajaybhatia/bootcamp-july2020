# Data Structures
'''
1. List
2. Tuple
3. Dictionary
4. Set
'''

# List -> Mutable
list = [1, 2, 3, 4, 5, 6, 7, 6, 8, 6]
print(list)

# To insert at the end
list.append(10)
print(list)

# To remove from end
list.pop()
print(list)

# To access an element
print(list[-1])

# To access multiple values (slicing)
print(list[::-1])

# To remove element by index
del list[2]
print(list)

# To remove specific element
list.remove(6)
print(list)

# To find index of an element
print(list.index(8))

# Add two lists using + operator
l1 = [1, 2, 3]
l2 = [4, 5, 6, 7]
print(l1.extend(l2))
print(l1)
print(l2)

print(6 in l1)
print(len(l1))
