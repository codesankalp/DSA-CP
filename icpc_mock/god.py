for i in range(int(input())):
    k = int(input())
    ls = list(map(int, input().split()))
    n = max(ls)*(min(ls))
    print("Case {}: {}".format(i+1, n))
