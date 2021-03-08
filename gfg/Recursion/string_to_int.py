#Covert a given string to integer using recursion.

def str_to_int(s):
	if len(s) == 0 or len(s) == 1:
		return int(s)
	return int(s[-1]) + str_to_int(s[:-1])*10

print(str_to_int('5467'))