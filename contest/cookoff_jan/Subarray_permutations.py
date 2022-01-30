for _ in range(int(input())):
    n, k = map(int, input().split())
    if n == 1 and k == 1:
        print(1)
    elif n > 1 and k == 1:
        print(-1)
    else:
        for i in range(1, k):
            print(i, end=' ')
        for i in range(k, n+1)[::-1]:
            print(i, end=' ')
        print()
