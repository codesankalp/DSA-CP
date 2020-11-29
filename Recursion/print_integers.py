# >Given a positive integer `n`, write a function, `print_integers`, that uses recursion to print all numbers from `n` to `1`. 
# >For example, if `n` is `4`, the function shuld print `4 3 2 1`. 

def print_integers(n):
	if n<=0:
		return
	print(n,end=" ")
	print_integers(n-1)

print_integers(5)

# time complexity :- 𝑇(𝑛)=𝑛𝑘