# https://www.codechef.com/problems/RIGHTRI

def dis(x, y, a, b):
    return ((x-a)**2+(y-b)**2)**(1/2)


ans = 0
for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3 = list(map(int, input().split()))
    a = dis(x1, y1, x2, y2)
    b = dis(x2, y2, x3, y3)
    c = dis(x3, y3, x1, y1)
    print(a, b, c)
    if a**2 == b**2+c**2 or c**2 == b**2+a**2 or b**2 == a**2+c**2:
        ans += 1
print(ans)
