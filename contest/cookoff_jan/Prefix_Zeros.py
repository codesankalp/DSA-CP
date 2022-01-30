def get_prefix(s, m):
    prefix = 0
    i = m
    while(i >= 0):
        v = (int(s[i])-int('0') + prefix) % 10
        if v == 0:
            i -= 1
            continue
        prefix += 10-v
        i -= 1
    return prefix


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    l = 0
    r = n-1
    lps = 0
    while l <= r:
        m = int((l+r)//2)
        add = 0
        if get_prefix(s, m) > k:
            r = m-1
        else:
            lps = m+1
            l = m+1
    print(lps)
