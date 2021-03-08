# Check whether the elements in array is sorted or not (USING RECURSION)

def check_sort(arr):
	if len(arr) == 1 or len(arr) == 0:
		return True
	return arr[0]<arr[1] and check_sort(arr[1:])

arr = [1,2,3,4,5]
print(check_sort(arr))
