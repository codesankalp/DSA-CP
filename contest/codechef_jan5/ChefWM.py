for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = 0
    temp = m
    i = 2
    while i * i <= m:
        if not temp % i:
            ans += 1
            while not (temp % i):
                temp /= i
        i += 1

    if temp > 1:
        ans += 1

    ls = []
    i = 1
    while i * i <= n:
        if not (n % i):
            ls.append(i)
            if i != n // i:
                ls.append(n // i)
        i += 1
    val = 0
    for x in ls:
        if x <= ans:
            val = x
    print(val)
