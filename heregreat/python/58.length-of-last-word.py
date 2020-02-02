#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = 0
        res = [0]
        for i in range(len(s)):
            if(s[i] == ' '):
                if(start > 0):
                    res.append(start)
                start = 0
            else:
                start += 1
        if(start > 0):
            res.append(start)
        return res[-1]
# @lc code=end

