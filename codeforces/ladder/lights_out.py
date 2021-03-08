toggle = list()
mat = list()
for i in range(3):
    row = list(map(int,input().split()))
    mat.append(row)
    toggle.append(row)
for i in range(3):
    for j in range(3):
        if mat[i][j] != 0:
            if i == 0 and j == 0 :
                toggle[i][j+1] += mat[i][j]
                toggle[i+1][j] += mat[i][j]
                
            elif i == 1 and j==0:
                toggle[i][j+1] += mat[i][j]
                toggle[i+1][j] += mat[i][j]
                toggle[i-1][j] += mat[i][j]
                
            elif i==2 and j==0:
                toggle[i][j+1] += mat[i][j]
                toggle[i-1][j] += mat[i][j]
                
            elif i==0 and j==1:
                toggle[i][j+1] += mat[i][j]
                toggle[i+1][j] += mat[i][j]
                toggle[i][j-1] += mat[i][j]
                
            elif i==1 and j==1:
                toggle[i][j+1] += mat[i][j]
                toggle[i+1][j] += mat[i][j]
                toggle[i][j-1] += mat[i][j]
                toggle[i-1][j] += mat[i][j]
            
            elif i==2 and j==1:
                toggle[i][j+1] += mat[i][j]
                toggle[i][j-1] += mat[i][j]
                toggle[i-1][j] += mat[i][j]
                
            elif i==0 and j==2:
                toggle[i+1][j] += mat[i][j]
                toggle[i][j-1] += mat[i][j]
                
            elif i==1 and j==2:
                toggle[i-1][j] += mat[i][j]
                toggle[i+1][j] += mat[i][j]
                toggle[i][j-1] += mat[i][j]
                
            elif i ==2 and j==2:
                toggle[i][j-1] += mat[i][j]
                toggle[i-1][j] += mat[i][j]
for i in toggle:
    for j in i:
        if j%2==0:
            print(0,end="")
        else:
            print(1,end="")
    print()
