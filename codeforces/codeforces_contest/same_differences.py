for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    d = {}
    for i, j in enumerate(ls):
        d[j-i] = d.get(j-i, 0) + 1
    cnt = 0
    for k, v in d.items():
        if v > 1:
            cnt += (v)*(v-1)/2
    print(int(cnt))

# 3 4 - 1  2 1
