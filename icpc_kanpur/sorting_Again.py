for _ in range(int(input())):
    n = int(input())
    # nls = [0]*1001
    ls = (list(map(int, input().split())))
    a = set(ls)
    if len(ls)!=len(a):
        print("NO")
    else:
        print("YES")
