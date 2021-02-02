# https://www.codechef.com/problems/PCYCLE
n = int(input())
ls = list(map(int, input().split()))
# 2 4 5 1 7 6 3 8
visited = [0]*n
ans = []
i = visited.index(0)+1
match = i
ans = []
ans.append(i)
count = 0
while True:
    visited[ls.index(ls[i-1])] = 1
    ans.append(ls[i-1])
    i = ls[i-1]
    if i == match:
        ans.append(0)
        try:
            i = visited.index(0)+1
            match = i
            ans.append(i)
        except:
            break
print(ans.count(0))
for i in ans:
    if i == 0:
        count += 1
        print()
        continue
    print(i, end=" ")
