for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if i==0:
            ans.append(ls[i]&ls[i+1])
        elif i==n-1:
            ans.append(ls[i]&ls[i-1])
        else:
            ans.append(max(ls[i]&ls[i-1], ls[i]&ls[i+1]))
    print(*ans)

