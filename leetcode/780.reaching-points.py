#
# @lc app=leetcode id=780 lang=python3
#
# [780] Reaching Points
#

# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx<tx and sy<ty:
            # (a+b) % a = b
            tx, ty = tx%ty, ty%tx

        if (sx==tx and sy<=ty and (ty-sy)%sx==0) or ((sy==ty and sx<=tx and (tx-sx)%sy==0)):
            return True
        return False
# @lc code=end

