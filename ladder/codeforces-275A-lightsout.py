arr = []
for i in range(3):
    arr.append([1,1,1])

mat = list()
for i in range(3):
    row = list(map(int,input().split()))
    mat.append(row)
    
for i in range(3):
    for j in range(3):
#         print(mat,arr,sep="\n")
#         print("=========================")
        if mat[i][j]%2 != 0:
            if arr[i][j]: arr[i][j]=0
            else:arr[i][j] = 1
            if i!=0:
                if arr[i-1][j]:arr[i-1][j]=0
                else:arr[i-1][j]=1
            if i!=2:
                if arr[i+1][j]:arr[i+1][j]=0
                else:arr[i+1][j]=1
            if j!=2:
                if arr[i][j+1]:arr[i][j+1]=0
                else:arr[i][j+1]=1
            if j!=0:
                if arr[i][j-1]:arr[i][j-1]=0
                else:arr[i][j-1]=1
            
for i in arr:
    for j in i:
        print(j,end="")
    print()
