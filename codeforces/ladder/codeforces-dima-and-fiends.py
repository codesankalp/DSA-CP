n = int(input())
ls = list(map(int, input().split()))
friends = sum(ls)
nls = []
for i in range(friends):
    if i%(n+1)==0:
        nls.append('B')
    else:
        nls.append(0)
for i in range(5):
    if (friends+i)%(n+1)==0:
        nls.append('B')
    else:
        nls.append(0)
# print(nls)
print(nls[friends:].count(0))
