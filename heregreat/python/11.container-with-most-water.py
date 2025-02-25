#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        res = 0
        while(i < j):
            cov = (j - i) * min(height[i], height[j])
            res = max(res, cov)
            if(height[i] <= height[j]):
                i += 1
            else:
                j -= 1
        return res
# @lc code=end

