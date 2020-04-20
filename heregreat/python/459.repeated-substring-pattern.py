#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2, 0, -1):
            if(len(s) % i == 0):
                num = len(s) // i
                strs = ""
                for _ in range(num):
                    strs += s[0:i]
                if(strs == s):
                    return True
        return False
# @lc code=end

