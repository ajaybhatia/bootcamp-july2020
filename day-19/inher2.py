class Employee:
	def __init__(self, id, name):
		self.id = id
		self.name = name


class Manager(Employee):
	def __init__(self, id, name):
		Employee.__init__(self, id, name)


class Labourer(Employee):
	def __init__(self, id, name):
		Employee.__init__(self, id, name)
