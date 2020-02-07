#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if(len(grid) == 0 or len(grid[0]) == 0):
            return 0
        dp = [[0]*len(grid[0]) for _ in grid]
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            if(i > 0):
                dp[i][0] = grid[i][0] + dp[i-1][0]
        for i in range(len(grid[0])):
            if(i > 0):
                dp[0][i] = grid[0][i] + dp[0][i-1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(i > 0 and j > 0):
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
# @lc code=end

