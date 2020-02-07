#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
from typing import List
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if(len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0 or obstacleGrid[0][0] == 1):
            return 0
        dp = [0 for _ in obstacleGrid[0]]
        dp[0] = 1
        for i in obstacleGrid:
            index = 0
            for j in i:
                if(j == 1):
                    dp[index] = 0
                elif(index > 0):
                    dp[index] += dp[index - 1]
                index += 1
        return dp[-1]
# @lc code=end
print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
