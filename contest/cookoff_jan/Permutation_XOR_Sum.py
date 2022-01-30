def inverse(n):
    num = 0
    count = 0
    while n:
        if n % 2 == 0:
            num += 1 << count
        n //= 2
        count += 1
        if n <= 0:
            break
    return num


for _ in range(int(input())):
    n = int(input())
    ans = 0
    while n > 0:
        inv = inverse(n)
        temp = n
        if (temp & (temp+1)) == 0:
            temp -= 1
        sum_ = ((temp * (temp+1)) // 2) - ((inv * (inv-1)) // 2)
        ans += sum_*2
        n = inv-1
    print(ans)
    # if n == 1:
    #     print(0)
    # else:
    #     ans = 0
    #     if (n % 2) != 0:
    #         n = n-1
    #     while n > 1:
    #         if n % 2 != 0:
    #             n -= 1
    #             continue
    #         ans += (n ^ (n-1))*2
    #         # print(n, n-1, (n ^ (n-1))*2)
    #         n //= 2
    #     print(ans)
