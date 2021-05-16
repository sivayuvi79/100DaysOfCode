#Array - Sorting - Insertion Sort:
class InsertionSort():

	def __init__(self, unsorted_list):

		self.unsorted_list = unsorted_list

	def solution(self):

		result = self.unsorted_list

		for i in range(1, len(result)):
			key = result[i]
			j = i - 1
			
			while j >= 0 and result[j] > key:
				result[j+1] = result[j]
				j -= 1

			result[j+1] = key

		return result

if __name__ == '__main__':

	number_of_tests = int(input("Enter the number of test cases: "))
	test_cases = []

	for i in range(1, number_of_tests+1):
		test_cases.append(list(map(int, input().split(','))))

	for j in test_cases:
		obj = InsertionSort(j)
		print(obj.solution())

	print("Please verify your result")
