#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        m = abs(dividend)
        n = abs(divisor)
        if((dividend < 0) ^ (divisor < 0)):
            sign = -1
        else:
            sign = 1
        if(m < n):
            return 0
        while(m >= n):
            t = n
            rev = 1
            while(m >= (t <<1)):
                t = t << 1
                rev = rev << 1
            res += rev
            m -= t
        if(sign == 1 and res > 2147483647):
            return 2147483647
        elif(sign == 1 and res <= 2147483647):
            return res
        elif(sign == -1):
            return -res
# @lc code=end

