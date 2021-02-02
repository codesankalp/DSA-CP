def ans(a, b, n):
    while b <= a and a >= 0 and b <= n:
        if b == a:
            return True
        b += k
        a -= k
    return False


for _ in range(int(input())):
    x, y, k, n = list(map(int, input().split()))
    a = max(x, y)
    b = min(x, y)
    if ans(a, b, n):
        print("Yes")
    else:
        print("No")
