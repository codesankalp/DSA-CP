n, m = list(map(int, input().split()))
ls = list(map(int, input().split()))
nls = []
for i in range(len(ls)):
    nls.append((i+1, ls[i]))
# print(nls)
if len(nls) == 1:
    print(1)
while len(nls) != 1:
    tls = []
    for (i,j) in nls:
        if j-m>0:
#             print((i,j))
            tls.append((i, j-m))
    nls = tls
    a = False
    if nls == []:
        print((len(ls)))
        break
    for i,j in nls:
        if j>m:
            a=True
    if a==False:
        print(list(nls)[-1][0])
        break
    if len(nls) == 1:
        print(list(nls)[-1][0])
#     print(nls)
