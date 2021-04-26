class Solution:
    def pivotIndex(self, nums) -> int:
        n = len(nums)
        s = sum(nums)
        l_s = 0
        for i in range(n):
            s -= nums[i]
            if l_s == s:
                return i
            l_s += nums[i]
        return -1

nums = list(map(int, input().split()))
a = Solution().pivotIndex(nums)
print(a)