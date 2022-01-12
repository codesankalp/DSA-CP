for _ in range(int(input())):
    m, x = map(int, input().split())
    ls = [0]*(x+1)
    ls[1] = 1
    for i in range(2, x+1):
        temp = m % i
        if temp == 0:
            temp = i
        ls[i] = ls[i-1]
        if ls[i] >= temp:
            ls[i] += 1
    for i in range(1, x+1):
        print(ls[i], end=" ")
    print()
