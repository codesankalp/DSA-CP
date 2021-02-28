for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    cnt = 0
    ls = [0]*n
    for i in range(n):
        if s[i] > 1:
            for j in range(i+2, min(i+s[i]+1, n)):
                ls[j] += 1
            if ls[i] > s[i]-1 and i != n-1:
                ls[i+1] += ls[i] - s[i] + 1
            cnt += max(s[i]-ls[i]-1, 0)
        elif i != n-1:
            ls[i+1] += ls[i]
    print(cnt)
