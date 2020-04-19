#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        wro = set()
        for i in range(0, len(s)):
            if(s[i] not in s[i+1:] and s[i] not in wro):
                return i
            else:
                wro.add(s[i])
        return -1

# @lc code=end
print(Solution().firstUniqChar("cc"))
