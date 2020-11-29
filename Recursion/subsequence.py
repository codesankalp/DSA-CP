# Print subsequences of given string using recursion.eg. if string is "abc" then output should be- " " "a" "b" "c" "ab" "bc" "ca" "abc",
# Note:Combinations of subsequence 2^N( here N is number of char in a given string)

def sub(s, curr='', index=0):
	if index == len(s):
		print(curr, end=" ")
		return
	sub(s,curr, index+1)
	# print(index)
	sub(s,curr+s[index], index+1)

sub("ABC")

# * - good question
'''
							  curr = ''
														index = 0 / appending A & ''
				''								'A'
																index = 1 / appending B & ''
		''				'B'				'A'				'AB'
																		index = 2 / appending C & ''
	''		'C'		'B'		'BC'	'A'		'AC'	'AB'	'ABC'		
																				index = 3 / STOP

'''
