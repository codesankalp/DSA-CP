# Given an integer, write a function that returns true if the given number is a palindrome, else false.
# For example, 12321 is a palindrome, but 1451 is not a palindrome.(USING RECURSION)

# c or cpp approach
def check_palindrome(s):
	return check_palindrome_func(s, 0, len(s)-1)

def check_palindrome_func(s, start_index, end_index):
	if start_index == end_index:
		return True
	if s[start_index] != s[end_index]:
		return False
	if start_index < end_index+1:
		return check_palindrome_func(s, start_index+1, end_index-1)
	return True

# my method
def is_palindrome(input):
    if len(input) <= 1:
        return True
    else:
        first_char = input[0]
        last_char = input[-1]
        sub_input = input[1:-1]
        return (first_char == last_char) and is_palindrome(sub_input)

s = input()
ans = check_palindrome(s)
ans2 = is_palindrome(s)
print(ans,ans2)