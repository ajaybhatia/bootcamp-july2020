# Immutable
t1 = ('apple', 'banana', 'grapes', 'pineapple', 3, 78, 8.12)
print(t1[::-1])

t2 = (10,)

print(type(t1))
print(type(t2))
print(len(t1))

print(t1 + t2)
print('banana' in t1)

# Unpacking/destructing of tuple
a, b, c = (10, 20, 30)
print(a)
print(b)
print(c)


a, *b, c = (10, 20, 30, 40, 50, 60)
print(a, b, c)
