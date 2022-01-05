for _ in range(int(input())):
    n, x, y = map(int, input().split())
    a, b = [(n+1)/2]*2
    print(int(abs(x-a)+abs(y-b))%2)