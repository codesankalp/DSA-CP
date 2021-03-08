# Write Python code to find if all the numbers in a given list of integers 
# are part of the series defined by the following.
# f(0) = 0 f(1) = 1 f(n) = 6*f(n-1) - 2*f(n-2) 
# for all n > 1. def is_part_of_series(lst):

def check(n):
	if n<0:
		return False
	if n==0 or n==1:
		return True
	fn_2=0
	fn_1=1
	fn = 6*fn_1 -2*fn_2
	while fn<=n:
		if fn==n:
			return True
		fn_2 = fn_1
		fn_1 = fn
		fn = 6*fn_1 -2*fn_2
	return False


def is_part_of_series(lst):
	for n in lst:
		if not check(n):
			return False
	return True


def f(n):
	if n==0:
		return 0
	if n==1:
		return 1
	return 6*f(n-1) -2*f(n-2)
