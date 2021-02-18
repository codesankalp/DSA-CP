for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ls = list(set(a))
    if len(ls) == len(a):
        print(n)
    else:
        nls = []
        for i in ls:
            nls.append(a.count(i))
        # print(nls)
        d = {}
        for i in nls:
            d[i] = d.get(i, 0) + 1
        ans = 0
        for i in d.values():
            ans = max(ans, i)
        print(ans)
