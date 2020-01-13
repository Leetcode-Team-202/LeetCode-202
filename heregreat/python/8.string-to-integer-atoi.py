#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        sign = 1
        max_int, min_int = 2147483647, -2147483648
        result, pos = 0, 0
        ls = len(str)
        while pos < ls and str[pos] == ' ':
            pos += 1
        if pos < ls and str[pos] == '-':
            sign = -1
            pos += 1
        elif pos < ls and str[pos] == '+':
            pos += 1
        while pos < ls and ord(str[pos]) >= ord('0') and ord(str[pos]) <= ord('9'):
            num = ord(str[pos]) - ord('0')
            result = result * 10 + num
            pos += 1
            if(result > max_int and sign == 1):
                return max_int
            elif(sign == -1 and result * sign < min_int):
                return min_int
        return sign * result
# @lc code=end

