def print_name(name):
	print(name)

# Higher order functions/Functions as first class citizens in pythons
# Functional programming (lambda functions)
def call_twice(func, name):
	func(name)
	func(name)

call_twice(print_name, "Ajay")