n = int(input())
vec = []
for i in range(n):
    vec.append(list(map(int,input().split())))
sum1 = 0    
for i in range(n):
    sum1 += vec[i][0]
sum2 = 0
for i in range(n):
    sum2 += vec[i][1]
sum3 = 0
for i in range(n):
    sum3 += vec[i][2]
if sum1 == 0 and sum2 == 0 and sum3==0:
    print("YES")
else:
    print("NO")