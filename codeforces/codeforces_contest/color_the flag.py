for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    ls = []
    for i in range(n):
        ls.append(input())
    nls = []
    for i in range(n):
        s = ''
        ans = "YES"
        for j in range(m):
            if ls[i][j] == '.':
                if j<m-1:
                    if ls[i][j+1] == '.':
                        pass
                    if ls[i][j+1] == 'R':
                        s += 'W'
                    else:
                        s += 'R'
                if i<n-1:
                    if ls[i+1][j] == '.':
                        pass
                    if ls[i+1][j] == 'R':
                        s += 'W'
                    else:
                        s += 'R'
                if j>0:
                    if ls[i][j-1] == '.':
                        pass
                    if ls[i][j-1] == 'R':
                        s += 'W'
                    else:
                        s += 'R'
            if ls[i][j] == 'R':
                if j<m-1:
                    if ls[i][j+1] == '.':
                        s += 'W'
                    if ls[i][j+1] == 'R':
                        ans = "NO"
                        break
                    else:
                        pass
                if i<n-1:
                    if ls[i+1][j] == '.':
                        pass
                    if ls[i+1][j] == 'R':
                        ans = "NO"
                        break
                    else:
                        pass
                if j>0:
                    if ls[i][j-1] == '.':
                        pass
                    if ls[i][j-1] == 'R':
                        ans = "NO"
                        break
                    else:
                        pass
            nls.append(s)
        print(nls, ans)


                
