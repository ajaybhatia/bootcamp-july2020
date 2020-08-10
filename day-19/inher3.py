class A:
	def __init__(self):
		print("Inside constructor of class A")


class B:
	def __init__(self):
		print("Inside constructor of class B")


class C(B, A):
	def __init__(self):
		print("Inside constructor of class C")


c = C()	