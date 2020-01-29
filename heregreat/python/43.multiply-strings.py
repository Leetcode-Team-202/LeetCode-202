#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = 0
        up = 0
        for i in num1:
            down = 0
            for j in num2:
                sum = int(i) * int(j) * pow(10, up + down)
                res += sum
                down += 1
            up += 1        
        return str(res)
# @lc code=end

res = Solution().multiply('123', '456')
print(res)
