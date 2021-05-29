def majority_elemnet_index(lst):

	from collections import Counter
	majority_elemnet = Counter(lst).most_common(1)
	element_index = []
	for i, j in enumerate(lst):
		if j == majority_elemnet[0][0]:
			element_index.append(i)
	if element_index == [0] : 
		element_index = []
	return element_index
print(majority_elemnet_index([1,1,2]))
print(majority_elemnet_index([1,2]))
print(majority_elemnet_index([]))
print(majority_elemnet_index([1,2,3,3,3,2,5,6]))