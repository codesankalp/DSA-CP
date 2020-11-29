n = int(input())
total = 0
ans = 0
for i in range(n):
    a,b = list(map(int, input().split()))
    total -= a
    total += b
    ans = max(total, ans)
print(ans)