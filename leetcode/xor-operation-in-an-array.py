class Solution:
    def xorOperation(self, n, start):
        nums = list(range(start, 2*n+start, 2))
        for i in range(n-1):
            nums[i+1] = nums[i]^nums[i+1]
        return nums[-1]



n = int(input('n: '))
start = int(input('start: '))

a = Solution()
ans = a.xorOperation(n, start)
print(ans)
