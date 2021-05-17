class Stack():

	"""Stack is the user defined data structure
	But in python list data structure provide same
	as Stack, the most recent inserted element should
	came out first"""

	def __init__(self):
		
		"""When we call a stack class
		it will create a empty list"""

		self.data = []

	def push(self, element):

		"""Here we are adding element at
		end of list, Just like a stack push"""
		self.data.append(element)

		return self.data

	def pop(self):

		"""Here we are removing first element of list
		Why because Stack usually follow LIFO logic"""
		self.data.pop()

		return self.data

	def peek(self):

		"""Here we will display last element of the stack"""

		return self.data[-1]

if __name__ == "__main__":
	stack = Stack()
	print(stack.push(5), "stack push")
	print(stack.push(8), "stack push")
	print(stack.pop(), "stack pop")
	print(stack.push(9), "stack push")
	print(stack.peek(), "stack peek")