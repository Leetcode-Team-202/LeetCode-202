#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []
        a = list(reversed(list(a)))
        b = list(reversed(list(b)))
        for i in range(max(len(a), len(b))):
            if(i < min(len(a), len(b))):
                sum = (ord(a[i]) - ord('0')) + (ord(b[i]) - ord('0')) + carry
            elif(len(a) > len(b)):
                sum = (ord(a[i]) - ord('0')) + carry
            elif(len(a) < len(b)):
                sum = (ord(b[i]) - ord('0')) + carry
            carry = sum // 2
            res.append(str(sum % 2))
        if(carry == 1):
            res.append('1')
        res = ''.join(reversed(res))
        return res
# @lc code=end
print(Solution().addBinary("1", "111"))
