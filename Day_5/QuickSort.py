class QuickSort():

	def __init__(self, arr):
		self.arr = arr

	def solution(self):
		#p is lower index
		#r is nth index
		#q is pivot, it can be any index
		p = 0
		r = len(arr)-1

		def partition(arr, p, r):

			i = p-1
			for j in range(p, r):
				if arr[j] <= arr[r]:
					i+=1
					arr[i], arr[j] = arr[j], arr[i]
			arr[i+1], arr[r] = arr[r], arr[i+1]
			return i+1

		def quick_sort(arr, p, r):
			
			if p<r:
				q = partition(arr, p, r)
				quick_sort(arr, p, q-1)
				quick_sort(arr, q+1, r)

		quick_sort(arr, p, r)

		return arr

if __name__ == '__main__':
	arr = [1,4,2,5]
	obj = QuickSort(arr)
	print(obj.solution())