class Solution:
    def maxAscendingSum(self, nums):
        n = len(nums)
        max_sum, sum_cnt = 0, 0
        for i in range(n):
            sum_cnt += nums[i]
            max_sum = max(sum_cnt, max_sum)
            try:
                if nums[i+1]<=nums[i]:
                    sum_cnt = 0
            except:
                pass
        return max_sum

a = Solution()
nums = list(map(int, input().split()))
ans = a.maxAscendingSum(nums)
print(ans)
