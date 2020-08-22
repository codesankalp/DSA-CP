# Remove consecutive duplicates from a string using recursion eg. if input is "aabbbcdd" output should be  "abcd"

def remove(s):
	arr = list(s)
	return remove_func(arr, 0, len(s)-1)

def remove_func(arr, start_index, end_index):
	if start_index >= end_index:
		return ''.join(arr)
	if arr[start_index] == arr[start_index+1]:
		arr[start_index] = ''
	return remove_func(arr, start_index+1, end_index)

print(remove('aabbccdd'))
