for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    j=ans=0
    for i in range(n):
        # print(a[i],b[i], ans, j)
        if(j==1 and (a[i]=='0' or b[i]=='0')):
            ans+=2
            j=0
        elif(j==2 and (a[i]=='1' or b[i]=='1')):
            if(a[i]=='1' and b[i]=='1'):
                ans+=1
            else:
                ans+=2
            j=0
        elif(a[i]=='1' and b[i]=='1'):
            j=1
        elif (a[i]=='0' and b[i]=='0'):
            ans+=1
            j=2
        elif ((a[i]=='0' and b[i]=='1') or (a[i]=='1' and b[i]=='0')):
            ans+=2
            j=0

    print(ans)

# 0 0
# 0 1
# 1 0
# 1 1
