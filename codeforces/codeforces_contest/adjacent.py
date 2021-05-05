def swap(mat, i, n):
    while(i < n):
        i += n


def shuffle(mat, n):
    for i in range(n):
        if i % 2 != 0:
            mat = swap(mat, i, n)
            print(mat)


for _ in range(int(input())):
    n = int(input())
    ls = list(range(1, n**2+1))
    print(ls)

# 1 5 3
# 4 8 6
# 7 2 9

# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16
