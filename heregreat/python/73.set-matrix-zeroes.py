#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
from typing import List
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dummy = '.'
        if(len(matrix) == 0 or len(matrix[0]) == 0):
            return
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if(matrix[i][j] == 0):
                    for _ in range(0, len(matrix)):
                        if(matrix[_][j] != 0):
                            matrix[_][j] = dummy
                    for _ in range(0, len(matrix[0])):
                        if(matrix[i][_] != 0):
                            matrix[i][_] = dummy
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if(matrix[i][j] == dummy):
                    matrix[i][j] = 0
# @lc code=end
print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
