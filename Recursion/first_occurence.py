# Find the first occurrence(index) of the element in a given array.
# (eg. array={2,3,5,6,7,6,7,5,6,1} let say element is 6 ,then the ans. should be 3(index)

def first_occur(arr, target):
	if len(arr) == 0:
		return -1
	if arr[0] == target:
		return 0
	if first_occur(arr[1:],target) == -1:
		return -1
	index = first_occur(arr[1:],target) + 1
	return index

res = first_occur([2,3,5,6,7,6,7,5,6,1], 3)
print(res)
