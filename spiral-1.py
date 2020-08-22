# Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.
def spiral(mat) : 
    m = len(mat)
    n = len(mat[0])
    i = 0
    j = 0

    while (i<m and j<n): 
        for k in range(j, n) : 
            print(mat[i][k], end = " ")      
        i += 1
 
        for k in range(i, m) : 
            print(mat[k][n - 1], end = " ")      
        n -= 1

        if ( i < m) :      
            for k in range(n - 1, (j - 1), -1) : 
                print(mat[m - 1][k], end = " ")               
            m -= 1
            
        if (j < n) : 
            for k in range(m - 1, i - 1, -1) : 
                print(mat[k][j], end = " ") 
            j += 1


mat = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
spiral(mat)