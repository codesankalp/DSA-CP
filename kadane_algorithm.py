# https://practice.geeksforgeeks.org/problems/kadanes-algorithm/1/?undefined

def maxSubArraySum(a):
    size = len(a)
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


print(maxSubArraySum(list(map(int, input().split()))))
