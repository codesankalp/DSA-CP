from math import gcd
from collections import deque

for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    nls = deque()
    for i in ls:
        if i % 2 == 0:
            nls.appendleft(i)
        else:
            nls.append(i)
    c = 0
    for i in range(len(nls)):
        for j in range(i+1, len(nls)):
            if gcd(nls[i], 2*nls[j]) > 1:
                c += 1
    print(c)


# ls = [6, 3, 5, 3]
# for i in range(len(ls)):
#     for j in range(i+1, len(ls)):
#         print(ls[i], ls[j], gcd(ls[i], 2*ls[j]) > 1, gcd(ls[i], 2*ls[j]))
