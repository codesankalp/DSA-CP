#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
import sys

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        m = len(nums2)
        max_n = sys.maxsize
        min_n = -(sys.maxsize)
        start = 0
        end = n
        partition_index = (n+m+1)//2
        while start <= end:
            partition_num1 = (start + end)//2
            partition_num2 = partition_index - partition_num1
            if partition_num1==0:
                max_left_nums1 = min_n
            else:
                max_left_nums1 = nums1[partition_num1-1]
            if partition_num1==n:
                min_right_nums1 = max_n
            else:
                min_right_nums1 = nums1[partition_num1]
            if partition_num2==0:
                max_left_nums2 = min_n
            else:
                max_left_nums2 = nums2[partition_num2-1]
            if partition_num2==m:
                min_right_nums2 = max_n
            else:
                min_right_nums2 = nums2[partition_num2]
            
            if (max_left_nums1<=min_right_nums2 and max_left_nums2 <= min_right_nums1):
                if ((n+m)%2==0):
                    return (min(min_right_nums1, min_right_nums2)+max(max_left_nums1, max_left_nums2))/2
                else:
                    return max(max_left_nums2, max_left_nums1)
            elif (max_left_nums1>min_right_nums2):
                end = partition_num1 -1
            else:
                start = partition_num1 +1


        
# @lc code=end

