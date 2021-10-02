#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def is_palindrome(self, ss):
        i=0
        j = len(ss)-1
        while(i<j):
            if ss[i]!=ss[j]:
                return False
            i+=1
            j-=1
        return True

    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                ss = s[i:j]
                if self.is_palindrome(ss):
                    count += 1
        return count
        
# @lc code=end

