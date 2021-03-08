n =  int(input())
pts = []
count = 0
for i in range(n):
    x,y = list(map(int, input().split()))
    pts.append((x,y))
for x,y in pts:
    a,b,c,d = [False]*4
    for i,j in pts:
        if (x,y) == (i,j):
            continue
        if i>x and j==y:
            a=True
        if i<x and j==y:
            b=True
        if i==x and j<y:
            c=True
        if i==x and j>y:
            d=True
    if [a, b, c, d] == [True]*4:
        count+=1
print(count)
