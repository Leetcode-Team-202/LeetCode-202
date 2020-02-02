#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
from typing import List
# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[' '] * n for _ in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1 ,0]
        r = c = di = 0
        fill = 1
        for _ in range(n * n):
            res[r][c] = fill
            cr, cc = r + dr[di], c + dc[di]
            if(cr < n and cc < n and res[cr][cc] == ' ' ):
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
            fill += 1
        return res        
# @lc code=end
print(Solution().generateMatrix(3))

