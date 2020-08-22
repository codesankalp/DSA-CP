# Remove a character from a given string using recursion

def remove(s,char):
	arr = list(s)
	return remove_func(arr, 0, len(s)-1, char)

def remove_func(arr, start_index, end_index, char):
	if start_index > end_index:
		return ''.join(arr)
	if arr[start_index] == char:
		arr[start_index] = ''
	return remove_func(arr, start_index+1, end_index, char)

print(remove('sankalp','s'))
