from math import ceil

for _ in range(int(input())):
    n,s = list(map(int, input().split()))
    # if n==1:
    #     print(s)
    # elif n>s:
    #     print("0")
    # # elif n==7:
    # #     print(4)
    # else:
    #     # ans = 0
    #     # print((s//(n-(round(n/2)-1))),round(s/(n-((n//2)-1))))
    #     if(n%2==0):
    #         print(int(s/((n/2)+1)))
    #     else:
    #         print(int(s/round(n/2)))
    print(int(s/(int(n/2)+1)))
