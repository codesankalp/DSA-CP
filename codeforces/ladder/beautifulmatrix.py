mat = []
for i in range(5):  
    mat.append(list(map(int,input().split())))
i, j = 0, 0
for row in range(len(mat)):
    if 1 in mat[row]:
        i, j = row , mat[row].index(1)

print(abs(i-2)+abs(j-2))