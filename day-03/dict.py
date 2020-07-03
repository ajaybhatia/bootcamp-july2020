# Dictionary
# Keys should be of type immutable

d = {10: "ten", 3.14: [1, 3, 3], (1, 0, 4): "some value"}
print(d[3.14])
print(d.get(10))

d[3.14] = "pie"

print(d)
print(d.keys())
print(d.values())
print(len(d))
print("ten" in d)
