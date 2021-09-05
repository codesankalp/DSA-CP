def sol(n):
    if n<100:
        if n%10 <=5:
            print((n%10)*2)
        else:
            print((n%10)-1)

for _ in range(int(input())):
    n = int(input())
    ls = []
    for i in range(1,10):
        ls.append((i, n%10**i))
        if n%(10**i)==n:
            print(n%10**i, i, n)
            break
    print(ls[:-1:])
    # for i in ls[:-1:]:
    if n<=100:
        if n%10 <=5:
            if n%10==0:
                print(9)
            else:
                print((n%10)*2)
        else:
            print((n%10)-1)
    # while ()


# 4 4
# 5 3
# 6 2
# 7 1

# 11 1
# 10 2
# 2 10
# 1 11

# 12 % 10 = 2
# (2, 12)


# 2021
# 1 _ 6 _

# _5 = 5

# 8->7
# 12->4


# 100 -> 9
# 2021 -> 44
# 10000 -> 99

# 21

# 1000 -> 0

# 2021%100=21
