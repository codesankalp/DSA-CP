from math import log
import sys
from copy import deepcopy

# def ans(n, x, l):
#     i = 1
#     j = 2
#     # while j <= n:
#     #     # print(l[i-1], i, j)
#     #     try:
#     #         p = int(log(l[i-1], 2))
#     #     except:
#     #         i += 1
#     #     # print(l[i-1], i, j)
#     #     a = 2**p
#     #     l[i-1] = l[i-1] ^ a
#     #     l[j-1] = l[j-1] ^ a
#     #     if l[i-1] == 0:
#     #         i += 1
#     #         j += 1

#     # while True:
#     # for q in range(1, n+1):
#     #     # print(i, j)
#     #     # if i >= n-1:
#     #     #     break
#     #     while l[i-1] == 0:
#     #         i += 1
#     #     # print(l[i-1])
#     #     p = int(log(l[i-1], 2))
#     #     a = 2**p
#     #     for j in range(i+1, n+1):
#     #         # print(i, j, a, l)
#     #         if l[j-1] > l[j-1] ^ a:
#     #             # j = i
#     #             break
#     #     else:
#     #         j = n
#     #     # print(i, j, a, l)
#     #     l[i-1] = l[i-1] ^ a
#     #     l[j-1] = l[j-1] ^ a

#     #     #
#     if n > 2:
#         while x > 0 and i <= n-1:

#             if l[i-1] == 0:
#                 p = 0
#             else:
#                 p = int(log(l[i-1], 2))
#             a = 1 << p
#             l[i-1] = l[i-1] ^ a
#             for j in range(i+1, n+1):
#                 c = l[j-1] ^ a
#                 if c < l[j-1]:
#                     l[j-1] = c
#                     break
#             else:
#                 l[-1] = c

#             while l[i-1] == 0 and l[i-1] <= n-1:
#                 i += 1

#             # print(l)
#             x -= 1
#     else:
#         for q in range(x):
#             if l[i-1] == 0:
#                 p = 1
#             else:
#                 p = 2**int(log(l[i-1], 2))
#             l[i-1] = l[i-1] ^ p
#             if n == 2:
#                 l[j-1] = l[j-1] ^ p
#             # print(l)

#     print(*l)


def ans(n, x, l):
    i = 1
    j = 2
    x2 = deepcopy(x)
    while x > 0 and i <= n-1:

        if l[i-1] == 0:
            p = 0
        else:
            p = int(log(l[i-1], 2))
        a = 1 << p
        l[i-1] = l[i-1] ^ a
        for j in range(i+1, n+1):
            c = l[j-1] ^ a
            if c < l[j-1]:
                l[j-1] = c
                break
        else:
            l[-1] = c

        while l[i-1] == 0 and l[i-1] <= n-1:
            i += 1
        x -= 1
        # print(*l)
    if l[n-1] == 0 and l[0] != 0 and x2 > n:
        i = 0
        j = n-1
        l[j] = l[i]
        l[i] = 0
    if n <= 2 and x % 2 != 0:
        i = 0
        j = 1
        l[i] = 1 ^ l[i]
        l[j] = 1 ^ l[j]

    print(*l)


# def ans(n, x, l):
#     i = 0
#     j = 1
#     x2 = deepcopy(x)
#     while i < n-1 and j < n and x > 0:
#         if l[j] == 0:
#             j += 1
#         if l[i] != 0:
#             if x <= n:
#                 p = int(log(min(l[i], l[j]), 2))
#             else:
#                 p = int(log(l[i], 2))
#             t = 1 << p
#             l[i] = t ^ l[i]
#             l[j] = t ^ l[j]
#             x -= 1
#         if l[i] == 0:
#             i += 1
#             j = i+1
#         print(l)
#     if l[n-1] == 0 and l[0] != 0 and x2 > n:
#         i = 0
#         j = n-1
#         l[j] = l[i]
#         l[i] = 0
#     if n <= 2 and x % 2 != 0:
#         i = 0
#         j = 1
#         l[i] = 1 ^ l[i]
#         l[j] = 1 ^ l[j]
#     print(*l)

# def ans(n, x, l):
#     i = 1
#     j = 2
#     while i <= n-1:
#         if l[i-1] == 0:
#             i += 1
#             continue
#         p = 2**int(log(l[i-1], 2))
#         for j in range(i+1, n+1):
#             pj = 2**int(log(l[j-1], 2))
#             if p == pj:
#                 l[i-1] = l[i-1] ^ p
#                 l[j-1] = l[j-1] ^ p
#             else:
#                 continue
#         else:
#             l[i-1] = l[i-1] ^ p
#             l[j-1] = l[j-1] ^ p

#     print(*l)


# for h in range(int(input())):
#     n, x = map(int, input().split())
#     a = list(map(int, input().split()))
#     i = 0
#     j = 1
#    # g = 0
#     while (x > 0) and (i < n-1):
#         if a[i] == 0:
#             p = 0
#         else:
#             p = int(math.log2(a[i]))
#         a[i] = a[i] ^ (1 << p)
#         for k in range(i+1, n):
#             c = a[k] ^ (1 << p)
#             if (c < a[k]):
#                 a[k] = c
#                 #j = k
#                 break
#         else:
#             a[-1] = c
#             #j = n-1

#         while (a[i] == 0) and (a[i] < n-1):
#             i += 1

#         if (n == 2):
#             i = 0
#         x -= 1
#     print(*a)

if __name__ == "__main__":
    for _ in range(int(input())):
        n, x = list(map(int, input().split()))
        l = list(map(int, input().split()))
        ans(n, x, l)
