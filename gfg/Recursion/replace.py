# Remove a character from a given string using recursion

def replace(s,char,rep):
	arr = list(s)
	return remove_func(arr, 0, len(s)-1, char, rep)

def remove_func(arr, start_index, end_index, char, rep):
	if start_index > end_index:
		return ''.join(arr)
	if arr[start_index] == char:
		arr[start_index] = rep
	return remove_func(arr, start_index+1, end_index, char, rep)

print(replace('sankalp','a','n'))
