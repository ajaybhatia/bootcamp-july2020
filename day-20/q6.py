'''
Question:
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
'''

import sys

class String:
	def __init__(self, str=""):
		self.str = str

	def getString(self):
		# i = 0 
		# for s in sys.argv:
		# 	if i != 0:
		# 		self.str += " " + s
		# 	i += 1
		self.str = ' '.join(sys.argv[1:])

	def printString(self):
		print(self.str.strip().upper())


s = String()

s.getString()
s.printString()

# str, i = "", 0 
# for s in sys.argv:
# 	if i != 0:
# 		str += " " + s
# 	i += 1

# print(str.strip().upper())

# str = ""
# for s in sys.argv[1:]:
# 	# str.join(s)
# 	print(s)

# print(' '.join(sys.argv[1:]))