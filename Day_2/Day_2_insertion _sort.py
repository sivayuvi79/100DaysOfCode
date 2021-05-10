#Array - Sorting - Insertion Sort:
class InsertionSort():

	def __init__(self, unsorted_list):

		self.unsorted_list = unsorted_list

	def solution(self):

		input_list = self.unsorted_list

		for i in range(1, len(input_list)):
			if input_list[i-1] > input_list[i]:
				temp = input_list[i-1]
				input_list[i-1] = input_list[i]
				input_list[i] = temp

		result = input_list

		return result

if __name__ == '__main__':
	number_of_tests = int(input("Enter the number of test cases"))
	# test_cases = [list(map(int, input("Enter the test case "+str(i)+""))) for i in number_of_tests]
	test_cases = [1, 2]
	for _ in test_cases:
		obj = InsertionSort(i)
		print(obj.solution(), "\n")

	print("Please verify your result")
