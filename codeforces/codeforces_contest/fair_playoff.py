for i in range(int(input())):
    ls = list(map(int, input().split()))
    s1, s2, s3, s4 = ls
    m = max(ls)
    ls.remove(m)
    m2 = max(ls)
    if (m in [s1, s2] and m2 in [s3, s4]) or (m2 in [s1, s2] and m in [s3, s4]):
        print("YES")
    else:
        print("NO")
