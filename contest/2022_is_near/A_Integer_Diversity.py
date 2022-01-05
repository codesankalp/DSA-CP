for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    nls = [0]*300
    for i in ls:
        nls[101+i] += 1
    d = set()
    for i in range(300):
        if nls[i]==0:
            continue
        if nls[i]==1:
            d.add(i-101)
        else:
            d.add(i-101)
            d.add(101-i)
    print(len(d))