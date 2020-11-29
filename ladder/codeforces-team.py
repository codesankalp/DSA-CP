n = int(input())
ans = 0
for i in range(n):
    ls = list(map(int, input().split()))
    if ls.count(0)>1:continue
    ans += 1
print(ans)
