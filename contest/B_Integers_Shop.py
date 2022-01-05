for _ in range(int(input())):
    cur_cost = 0
    for i in range(int(input())):
        l,r,c = map(int, input().split())
        if cur_cost!=c:
            cur_cost +=c
            if l==1:
                cur_cost=c
            print(cur_cost)
            if i!=0:
                cur_cost-=c
