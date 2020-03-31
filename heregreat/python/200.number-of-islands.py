#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if(len(grid)==0 or len(grid[0])==0):
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == '1'):
                    self.helper(grid, i, j)
                    res += 1

        return res
    def helper(self, grid, x, y):
        if(x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
            return
        if(grid[x][y] == '0'):
            return
        grid[x][y] = '0'
        self.helper(grid, x - 1, y)
        self.helper(grid, x + 1, y)
        self.helper(grid, x, y - 1)
        self.helper(grid, x, y + 1)
# @lc code=end
print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
