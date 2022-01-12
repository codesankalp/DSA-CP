for _ in range(int(input())):
    s, b = map(int, input().split())
    if s==1:
        if b%2==0:
            print("Even")
        else:
            print("Odd")
        continue
    if b%2==1:
        if s%2==0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Impossible")