t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    for i in range(n-1):
        if s[i+1] == s[i]:
            continue
        if s[i] in s[i+1:]:
            print("NO")
            break
    else:
        print("YES")