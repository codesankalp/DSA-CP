def get_even(n):
    return n//2


for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    less = min(a, b)
    if a == less:
        even = get_even(b)
        odd = b-even
    else:
        even = get_even(a)
        odd = a-even
    # for i in range(1, a+1):
    #     for j in range(1, b+1):
    #         if (i+j) % 2 == 0:
    #             print(i, j)
    #     print("-----")
    # print("=======")
    # ans = 0
    less_even = get_even(less)
    less_odd = less - less_even
    ans = less_even*even + less_odd*odd
    # for i in range(1, less+1):
    #     if i % 2 == 0:
    #         ans += even
    #     else:
    #         ans += odd
    print(ans)
