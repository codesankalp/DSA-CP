#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i,j in enumerate(nums):
            if j<1 or j>n:
                nums[i] = n+1
        
        for i,j in enumerate(nums):
            j = abs(j)
            if j>n:
                continue
            j -= 1
            if nums[j]>0:
                nums[j] = -1*nums[j]
        for i, j in enumerate(nums):
            if(j>=0):
                return i+1
        return n+1
        
# @lc code=end

