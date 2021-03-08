n = int(input())
finger = sum(list(map(int, input().split())))
ways = 0
for i in range(1,6):
    if (finger+i)%2==0:
        ways+=1
print(ways)
