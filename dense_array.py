for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ls = []
    ma = 0
    mi = 0
    ans = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            ma = a[i]
            mi = a[i+1]
        else:
            ma = a[i+1]
            mi = a[i]
        div = ma/mi
        if div > 2:
            ma = ma / 2
            while ma > mi:
                # print(ma, mi)
                ma = ma/2
                ans += 1
    print(ans)
