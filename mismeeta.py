def odd(m, ma):
    return int(ma**0.5) - int((m-1)**0.5)


# odd_n = [i**2 for i in range(1, 10**5+1)]
for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    nls = []
    for i in range(n):
        if ls[i]**0.5 == int(ls[i]**0.5):
            nls.append(i)

    if len(nls) <= 1:
        print(0)
    else:
        ans = 0
        for i in range(len(nls)-1):
            temp = nls[i+1] - nls[i] + 1
            if ans < temp:
                ans = temp
        print(ans)
    # nls = [0]*n
    # count = 0
    # for i in range(n):
    #     if ls[i] in odd_n:
    #         nls[i] = 1
    # # print(nls)
    # if nls.count(1) <= 1:
    #     print(0)
    # else:
    #     ans = []
    #     for i in nls:
    #         count += 1
    #         if i == 0:
    #             continue
    #         ans.append(count)
    #     # print(ans)
    #     a = max(ans)
    #     print(a - ans[ans.index(a)-1] + 1)


def getMaxCard(n, c):
    ec = []
    for i in range(n):
        if c[i]**0.5 == int(c[i]**0.5):
            ec.append(i)

    if len(ec) <= 1:
        return 0

    maxCard = ec[1] - ec[0] + 1
    for i in range(1, len(ec)-1):
        if maxCard < ec[i+1] - ec[i] + 1:
            maxCard = ec[i+1] - ec[i] + 1
    return maxCard
# Python3 program to find count
# of numbers having odd number
# of divisors in given range

# Function to count numbers
# having odd number of divisors
# in range [A, B]


def OddDivCount(a, b):

    # variable to odd divisor count
    res = 0

    # iterate from a to b and count
    # their number of divisors
    for i in range(a, b + 1):

        # variable to divisor count
        divCount = 0
        for j in range(1, i + 1):
            if (i % j == 0):
                divCount += 1

        # if count of divisor is odd
        # then increase res by 1
        if (divCount % 2):
            print(divCount, i)
            res += 1
    return res


# # Driver code
# if __name__ == "__main__":
#     a = 5
#     b = 12
#     print(OddDivCount(a, b))

# # This code is contributed
# # by ChitraNayal
