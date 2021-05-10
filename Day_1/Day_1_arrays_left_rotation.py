# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""
A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become . Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.
"""
class ArrayLeftRotation:

	def __init__(self, left_list, left_number):

		self.left_list = left_list
		self.left_number = left_number

	def solution(self):

		result = self.left_list
		d = self.left_number
		return result[d:] + result[:d]

if __name__ == '__main__':
	
	test_case_1 = ArrayLeftRotation([1, 2, 3, 4, 5], 4)
	test_case_2 = ArrayLeftRotation([10, 23, 21, 15, 17, 90, 100, 101], 7)
	print(test_case_1.solution())
	print(test_case_2.solution())