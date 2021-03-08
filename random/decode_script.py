import string
n, m = list(map(int, input().split()))
mat = []
for _ in range(n):
    l = list(input().split())
    mat.append(l)

ans = []
for i in range(m):
    for j in range(n):
        if (mat[j][i]).isalnum():
            ans.append(mat[j][i])

print(''.join(ans))
