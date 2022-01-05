import itertools

for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    nls = [0]*32
    # # print([i for i in itertools.product(range(n), repeat=2)])
    # for i,j in itertools.product(range(n), repeat=2):
    #     # if i+1<n:
    #     if not i<j:
    #         continue
    #     # print(i, i+1)
    #     nls.append(ls[i]&ls[i+1])
    # print(nls)
    for i in range(n):
        for j in range(32):
            nls[j] += ((ls[i]&(1<<j))>0)
    ans = 0
    for i in range(32):
        if nls[i]>=2:
            ans |= 1<<i
    print(ans)
