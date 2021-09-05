for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    cnt = a
    ans = 0
    # for i in range(0, a):
    #     ans = ans^i
    r = (a-1)%4
    if r==0:
        ans=a-1
    elif r==1:
        ans=1
    elif r==2:
        ans=a
    elif r==3:
        ans=0
    # print(ans,ans^b, cnt)
    if ans!=b:
        if (ans^b==a):
            cnt+=2
        else:
            cnt+=1
    print(cnt)