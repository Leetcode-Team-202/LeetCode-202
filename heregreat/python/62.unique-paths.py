#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """totally steps steps,the down step is n-1, so the possible unique paths is C(steps, n - 1)"""

        steps = (m - 1) + (n - 1)
        return self.cfact(steps, n - 1)

    def cfact(self, m , n):
        """calculate C(m, n)"""
        div = dic = 1
        for i in range(1, n + 1):
            div *= m
            dic *= i
            m -= 1        
        return div//dic
# @lc code=end

