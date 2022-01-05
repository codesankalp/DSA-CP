for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    s = input()

    ans = 0
    x = ord(s[0]) - ord('0')
    for i in range(1,n-k+1):
        x ^= ord(s[i]) - ord('0')
    if x==1:
        ans += 1
    for i in range(n-k+1, n):
        x ^= ord(s[i-n+k-1]) - ord('0')
        x ^= ord(s[i]) - ord('0')
        if (x==1):
            ans+=1
    print(ans)