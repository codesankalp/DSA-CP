#binary search using recursion

def binary_search(arr, target):
	arr = sorted(arr) #if array is not sorted
	return binary_search_func(arr, 0, len(arr)-1, target)


def binary_search_func(arr, start_index, end_index, target):
	if start_index > end_index:
		return -1 # element not found
	mid = (start_index+end_index) //2

	if arr[mid] == target:
		return mid
	elif arr[mid] > target:
		return binary_search_func(arr, start_index, mid-1, target)
	else:
		return binary_search_func(arr, mid+1, end_index, target)


arr = [1,2,3,4,5,6,7,8,9]
target = 5
res = binary_search(arr,target)
print(res)

# time complexity : T(n) = log(n)