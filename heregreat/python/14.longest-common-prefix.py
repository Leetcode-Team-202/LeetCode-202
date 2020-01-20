#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return ""
        res = ''
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in strs:
                if(i >= len(j) or j[i] != c):
                    return res
            res += c
        return res
# @lc code=end

