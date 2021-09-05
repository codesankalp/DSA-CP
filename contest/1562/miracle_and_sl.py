for _ in range(int(input())):
    a,b = list(map(int, input().split()))
    if (b-a>=a):
        print(b%(b//2+1))
    else:
        print(b%a)