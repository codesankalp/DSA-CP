for _ in range(int(input())):
    n,m = list(map(int, input().split()))
    a = []
    for i in range(m):
        a.append(input())
    st = []
    st.append(a[0])
    ans =0
    for i in range(m):
        if(i==0):
            continue
        k=0
        for j in range(len(st)):
            if(st[j]<a[i]):
                k+=1
        st.append(a[i])
        ans+=k
    print(ans)