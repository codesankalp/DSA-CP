for _ in range(int(input())):
    x = int(input())
    a = int(x**(1/3))
    for i in range(1, a):
        for j in range(1, a):
            print(i, j, x)
            if i**3 + j**3 == x:
                print("YES")
                break
    # else:
    #     print("NO")
