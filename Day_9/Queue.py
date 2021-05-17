class Queue():

	"""Queue is the user defined data structure
	But in python list data structure provide same
	as Queue with small modification, It follows FIFO
	like the first inserted element should come out first"""

	def __init__(self):
		
		"""When we call a Queue class
		it will create a empty list"""

		self.data = []

	def enque(self, element):

		"""Here we are adding element at
		end of list, Just like a Enqueue"""

		self.data.append(element)
		return self.data

	def deque(self):

		"""Here we are removing last element
		Why because Queue usually follow
		FIFO logic"""

		self.data.pop(0)
		return self.data

	def peek(self):

		"""Here we will display last element of the Queue"""

		return self.data[-1]

if __name__ == "__main__":
	queue = Queue()
	print(queue.enque(5), "Enqueue")
	print(queue.enque(8), "Enqueue")
	print(queue.deque(), "Dequeue")
	print(queue.enque(9), "Enqueue")
	print(queue.peek(), "Queue peek")