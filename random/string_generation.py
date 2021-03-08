for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    ls = []
    for i in range(n):
        ls.append(input())
    s = input()
    i = 0
    ans = True
    while len(s)!=i:
        if s[i] in ls[i%n]:
            ans = True
            ls[i%n] = ls[i%n].replace(s[i], '', 1)
        else:
            ans = False
            break
        i+=1
    if ans == True:
        print("Yes")
    else:
        print("No")
