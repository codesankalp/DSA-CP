#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start

def get_index(nums, target):
    i = j = -1
    i_prev = j_prev = -1
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = start + (end-start)//2
        if nums[mid]>=target:
            end = mid-1
        elif nums[mid]<target:
            start = mid + 1
        if nums[mid]==target:
            if i_prev!=mid or i!=-1:
                i_prev = i
                i = mid
            if i!=-1 and (j!=-1):
                j = mid
            if start<=end and j==-1 and i!=-1 or i_prev==mid:
                start = i
                end = len(nums)-1
        print(i, j, mid, start, end)
    return [i, j]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return get_index(nums, target)
        
# @lc code=end

