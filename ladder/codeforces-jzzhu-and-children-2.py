import math
n, m = list(map(int, input().split()))
ls = list(map(int, input().split()))
last = 0
val = 0
for i in range(n):
    if math.ceil(ls[i]/m) >= val:
        last = i+1
        val = math.ceil(ls[i]/m)
print(last)
