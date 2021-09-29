#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            k = ''.join(sorted(word))
            ans[k] = ans.get(k, []) + [word] 
        return ans.values()
# @lc code=end

