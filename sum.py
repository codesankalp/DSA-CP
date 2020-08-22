# Write a program to find sum of every row and every column in a two-dimensional
# array

def sum_row_column(mat):
	for i,row in enumerate(mat):
		print("sum of {} row is: {}".format(i,sum(row)))

	for i,row in enumerate(zip(*mat)):
		print("sum of {} column is: {}".format(i,sum(row)))


mat = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

sum_row_column(mat)