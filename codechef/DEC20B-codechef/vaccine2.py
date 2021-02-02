from math import ceil
for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    age = list(map(int, input().split()))
    risk = 0
    for i in age:
        if i >= 80 or i <= 9:
            risk += 1
    unrisk = n-risk
    ans = ceil(risk/d) + ceil(unrisk/d)
    print(ans)
