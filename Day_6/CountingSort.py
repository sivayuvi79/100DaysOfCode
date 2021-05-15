class CountingSort():

	def __init__(self, arr):

		self.arr = arr

	def solution(self):
		arr = self.arr
		print(arr)
		count = [0 for i in range(256)] 
		# the range between 256 number
		out_arr = [0 for a in range(0, len(arr)+1)]

		for j in range(0, len(arr)): count[arr[j]] = count[arr[j]] + 1

		for k in range(0, len(count)): count[k] = count[k] + count[k-1]

		for b in range(len(arr)-1, -1, -1):
			out_arr[count[arr[b]]] = arr[b]
			count[arr[b]] = count[arr[b]] - 1

		return out_arr[1:]

if __name__ == '__main__':
	test_array = [2,8,5,9,87,5,6,2,1,1,5,2]
	obj = CountingSort(test_array)
	print(obj.solution())