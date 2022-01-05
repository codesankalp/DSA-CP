for _ in range(int(input())):
    n = int(input())
    k=0
    if n==3:
        print(10)
    elif n>3:
        k = (3**(n-3))*8*(n-2)
        k+=k//4
        print(k)
    else:
        print(0)
