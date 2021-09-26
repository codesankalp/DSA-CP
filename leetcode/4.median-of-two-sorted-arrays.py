#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        mid = (n+m+1)//2
        i = mid//2
        while (not(nums1[i]<=nums2[mid-i] and nums2[i]<=nums1[mid-1])):
            print(nums1[i], nums2[i], nums1[mid-i], nums2[mid-i])
        nums1[mid]<=nums2[mid]
        
# @lc code=end

