for _ in range(int(input())):
    n = int(input())
    s = input()
    i=0
    ans = ""
    while(i<n):
        if s[i]=="L":
            ans += "LR"
            i+=1
        elif s[i]=="U":
            ans+="D"
        elif s[i]=="D":
            ans+="U"
        elif s[i]=="R":
            ans+="RL"
        i+=1
    print(ans)