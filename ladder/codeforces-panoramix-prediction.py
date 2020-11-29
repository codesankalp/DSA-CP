lower, upper = list(map(int,input().split()))

ls=[]
for num in range(lower,70):  
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                break  
        else:
            if num==lower:
                continue
            ls.append(num) 
# print(ls)
if ls[0]==upper:
    print("YES")
else:
    print("NO")
