#
# @lc app=leetcode id=537 lang=python3
#
# [537] Complex Number Multiplication
#

# @lc code=start
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        al = a.split('+')
        a1 = int(al[0])
        a2 = int(al[1][0:-1])
        bl = b.split('+')
        b1 = int(bl[0])
        b2 = int(bl[1][0:-1])

        res1 = a1 * b1 - a2 * b2
        res2 = a1 * b2 + a2 * b1
        res = str(res1) + '+' + str(res2) + 'i'
        return res
# @lc code=end

