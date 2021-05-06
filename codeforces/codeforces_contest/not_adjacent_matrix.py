def swap(mat, i, n):
    while(i < n**2):
        try:
            mat[i], mat[i+n] = mat[i+n], mat[i]
            i += n
        except:
            break
    # print("from swap", mat)
    return mat


def shuffle(mat, n):
    for i in range(n):
        if i % 2 != 0:
            mat = swap(mat, i, n)
            # print(mat)
    return mat


for _ in range(int(input())):
    n = int(input())
    ls = list(range(1, n**2+1))
    if n == 2:
        print(-1)
    else:
        # print(ls)
        mat = shuffle(ls, n)
        # print(ls, ls == mat)
        for i in range(n**2):
            print(mat[i], end=" ")
            if i % n == 0:
                print()


# 1 5 3
# 4 8 6
# 7 2 9

# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16

# 1 6 3 8
# 5 10 7 12
# 9 14 11 16
# 13 2 15 4
