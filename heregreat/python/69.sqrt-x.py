#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if(x <= 1):
            return x
        left = 0
        right = x
        while(left < right):
            mid = left + (right - left) // 2
            if(x // mid >= mid):
                left = mid + 1
            else:
                right = mid
        return right - 1
# @lc code=end

