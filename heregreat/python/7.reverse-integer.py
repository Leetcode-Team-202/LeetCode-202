#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res, ispos = 0, 1
        if(x < 0):
            ispos = -1
            x *= -1
        while(x!=0):
            res = res * 10 + x%10
            if(res > 2147483647):
                return 0
            x = int(x / 10)
        return res*ispos
# @lc code=end

