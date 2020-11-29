n,t = list(map(int,input().split()))
s = input()
ls = []
for i in s:
    ls.append(i)

for i in range(t):
    nls = ls.copy()
    for i in range(len(ls)-1):
        if ls[i] == 'B' and ls[i+1] == 'G':
            nls[i],nls[i+1] = nls[i+1],nls[i]
    ls = nls
print(''.join(nls))