n, n2 = list(map(int, input().split()))
a = list(map(int, input().split()))
one_count = a.count(1)
for _ in range(n2):
    t, q = list(map(int, input().split()))
    if t == 1:
        if a[q-1] == 1:
            one_count -= 1
        else:
            one_count += 1
        a[q-1] = 1 - a[q-1]
    elif t == 2:
        if q <= one_count:
            print(1)
        else:
            print(0)
