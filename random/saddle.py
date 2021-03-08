# Write a program to find a saddle point in a two-dimensional array. A saddle point in a
# numerical array is a number that is larger than or equal to every number in its column,
# and smaller than or equal to every number in its row.

def saddle(mat):
	for i in mat:
		minimum = min(i)

		for j in zip(*mat):	
			if max(j) == minimum:
				print(max(j))
				return True
	print("No Saddle Point")
	return False


mat = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

saddle(mat)