import math

for _ in range(int(input())):
    n,k = map(int, input().split())
    if k<=math.ceil(n/2):
        mat = [["."]*n for _ in range(n)]
        for i in range(k):
            mat[2*i][2*i] = "R"
        print(*["".join(j) for j in mat], sep="\n")
    else:
        print(-1)
