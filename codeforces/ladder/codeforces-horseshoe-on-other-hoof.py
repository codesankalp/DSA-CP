ls = list(map(int, input().split()))
ans = set()
for i in ls:
    ans.add(i)
print(4-len(ans))
