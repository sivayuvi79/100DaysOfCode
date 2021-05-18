class ProblemSolving():
	def __init__(self, arr):
		self.arr = arr
	def problem_1(self):

		"""Given an unsorted array of integers, 
		return the length of the longest 
		consecutive elements sequence."""
		arr = self.arr
		arr = sorted(list(set(arr)))
		# key = arr[0]
		check = []
		test = [arr[0]]

		for i in range(1,len(arr)):
			if arr[i] - arr[i-1] == 1:
				test.append(arr[i])
				if arr[i] != arr[-1]: continue;
			check.append(test)
			test = [arr[i]]

		return check

if __name__ == "__main__":
	test_array = [100,4,200,1,202,203,500,501,101,300,301,3,2]
	problem_solving = ProblemSolving(test_array)
	print(problem_solving.problem_1())


