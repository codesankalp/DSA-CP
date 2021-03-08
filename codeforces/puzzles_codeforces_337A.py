from sys import maxsize
n, m = list(map(int, input().split()))
puzzles = list(map(int, input().split()))
ls = sorted(puzzles)
i = 0
j = i+n-1
ans = maxsize
# print(ls)
while j<m:
    # print(i,j)
    ans = min(ans, ls[j]-ls[i])
    j+=1
    i+=1
print(ans)


# a,b=map(int,input().split())
# *c,=sorted(map(int,input().split()))
# q=9999999999999
# for i in range(b):
#     try:
#         if (z:=abs(c[i]-c[(a-1)+i]))<q:
#             q=z
#     except:0

# print(q)
