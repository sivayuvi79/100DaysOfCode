class HeapSort():

	def __init__(self, arr):
		self.arr = arr

	def max_heap_sort(self):
		arr = self.arr
		n = len(arr)

		def max_heapify(arr, n, i):
			l = 2 * i + 1# left(i)
			r = 2 * i + 2 #right(i)
			largest = i

			if l <n and arr[largest] < arr[l]:
				largest = l

			if r <n and arr[largest] < arr[r]:
				largest = r
				
			if largest != i:
				arr[i], arr[largest] = arr[largest], arr[i]
				max_heapify(arr, n, largest)

		for i in range(n//2-1, -1, -1):
			max_heapify(arr, i, n)

		for i in range(n-1, 0, -1):
			arr[i], arr[0] = arr[0], arr[i]  # swap
			max_heapify(arr, i, 0)

		return arr

if __name__ == '__main__':
	n = int(input("Enter the number of test cases"))
	test_cases = [list(map(int, input().split(','))) for i in range(n)]
	for j in test_cases:
		obj = HeapSort(j)
		print(obj.max_heap_sort())
