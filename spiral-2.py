def spiral_gen(a):
    if a <= 0:
        return []
    ans = [[None for i in range(a)] for j in range(a)]
    k,m = 0,a-1
    l,n = 0,a-1
    dir = 1
    while (True):
        for i in range(l,n+1):
            ans[k][i] = dir
            dir += 1
        k += 1
        if (k > m):
            break
        for i in range(k,m+1):
            ans[i][n] = dir
            dir += 1
        n -= 1
        if (n < l):
            break
        for i in range(n,l-1,-1):
            ans[m][i] = dir
            dir += 1
        m -= 1
        if (m < k):
            break
        for i in range(m,k-1,-1):
            ans[i][l] = dir
            dir += 1
        l += 1
        if (l > n):
            break
    return ans


a = int(input())
ans = spiral_gen(a)
print(ans)

# 1 2 3
# 8 9 4
# 7 6 5