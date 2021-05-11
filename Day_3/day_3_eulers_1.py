class EulersProblemOne():
	# Project Euler #1: Multiples of 3 and 5

	def __init__(self, num):

		self.num = num

	def solution(self):
		n = self.num
		n3 = (n-1)//3
		n5 = (n-1)//5
		n15 = (n-1)//15
		result = 3*(n3*(n3 + 1))//2 + 5*(n5*(n5 + 1))//2 - 15*(n15*(n15 + 1 ))//2
		return result

if __name__ == '__main__':

	number_of_tests = int(input("Enter the number of test cases: "))
	test_cases = [int(input()) for i in range(number_of_tests)]

	for j in test_cases:
		obj = EulersProblemOne(j)
		print(obj.solution())

	print("Please verify your result")

