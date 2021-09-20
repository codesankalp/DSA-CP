for _ in range(int(input())):
    s = input()
    ans=j=0
    for i in s:
        if(i=='0'):
            j=1
        elif (j==1 and i=='1'):
            ans+=1
            j=0
    if(s[-1]!='1'):
        ans+=1
    print(min(ans,2))