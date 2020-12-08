for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    j = 1
    arr = [-i for i in range(1, n+1)]
    arr[0] = 1
    for i in range(1, n):
        if j < k and sum(arr[:i]) < 0:
            j += 1
            arr[i] = -(arr[i])
    b = n-k
    # print(*arr, j)
    j = 0
    for i in range(n):
        if j < b and arr[i] < 0:
            j += 1
        elif arr[i] < 0:
            arr[i] = -(arr[i])
        else:
            pass
    print(*arr)
    # n, k = list(map(int, input().split()))
    # ls = []
    # if n % 2 == 0:
    #     for i in range(1, n+1):
    #         if i % 2 == 0:
    #             ls.append(-i)
    #         else:
    #             ls.append(i)
    # else:
    #     for i in range(1, n+1):
    #         if i % 2 == 0:
    #             ls.append(i)
    #         else:
    #             ls.append(-i)

    # count = 0
    # s = 0
    # for i in ls:
    #     s += i
    #     if s > 0:
    #         count += 1

    # if count == k:
    #     pass
    # elif count > k:
    #     for i in range(n, 1, -1):
    #         if count == k:
    #             break
    #         if ls[i-1] > 0:
    #             ls[i-1] = ls[i-1]*(-1)
    #             count -= 1
    # else:
    #     for i in range(1, n+1):
    #         if count == k:
    #             break
    #         if ls[i-1] < 0:
    #             ls[i-1] = ls[i-1]*(-1)
    #             count += 1

    # for j in ls:
    #     print(j, end=" ")
    # print()

# 5 3
# 1 2 -3 4 -5

# 1 2 - 3 4 5
