# Count the number of characters in a given string using recursion (eg.abcd ,output=4)

def length(s):
	if s == '':
		return 0
	return length(s[1:]) + 1

print(length('abcd'))
