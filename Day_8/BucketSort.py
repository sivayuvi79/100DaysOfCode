class BucketSort():

	def __init__(self, arr):
		self.arr = arr

	def insertion_sort(arr):

		for i in range(1, len(arr)):
			check = arr[i]
			j = i - 1
			while j>=0 and arr[j] > check:
				arr[j+1] = arr[j]
				j -= 1
			arr[j+1] = check
		return arr

	def bucket_sort(self):

		arr = self.arr
		n = len(arr)
		bucket = [[] for i in range(n)]
		for i in range(0, len(arr)): 
			bucket[int(n*arr[i])].append(arr[i])
		temp = [BucketSort.insertion_sort(j) for j in bucket] 
		result = []
		for k in temp:
			result += k 
		print(result)


if __name__ == "__main__":
	arr = [0.34,0.45,0.42,0.26,0.53,0.90]
	print(arr)
	obj = BucketSort(arr)
	print(obj.bucket_sort())


