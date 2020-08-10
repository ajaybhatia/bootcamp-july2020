class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area(self):
		return self.length*self.width

	def parameter(self):
		return 2 * (self.length+self.width)

class Square(Rectangle):
	def __init__(self, side):
		Rectangle.__init__(self, side, side)


rectangle = Rectangle(10, 20)
print(f"Area of rectangle is {rectangle.area()}")
print(f"Parameter of rectangle is {rectangle.parameter()}")

square = Square(10)
print(f"Area of square is {square.area()}")
print(f"Parameter of square is {square.parameter()}")
