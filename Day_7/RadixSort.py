class RadixSort():

	def __init__(self, arr):
		self.arr = arr

	def counting_sort(arr, exp1):

		n =len(arr)
		output = [0] * (n)	 
		count = [0] * (10)
	 
		for i in range(0, n):
			index = (arr[i] / exp1)
			count[int(index % 10)] += 1
	 
		for i in range(1, 10):
			count[i] += count[i - 1]
	 
		i = n - 1
		while i >= 0:
			index = (arr[i] / exp1)
			output[count[int(index % 10)] - 1] = arr[i]
			count[int(index % 10)] -= 1
			i -= 1
	 
		i = 0
		for i in range(0, len(arr)):
			arr[i] = output[i]

		return arr

	def solution(self):
		arr = self.arr
		max_element = 0

		for i in arr:
			if i > max_element:
				max_element = i

		n = len(str(max_element))
		exp = 1

		for j in range(1, n+1):
			arr = RadixSort.counting_sort(arr, exp)
			exp *= 10
			
		return arr

if __name__ == '__main__':
	test_array = [2,98,45,66,37,101,203]
	obj = RadixSort(test_array)
	print(obj.solution())