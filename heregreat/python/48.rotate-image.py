#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
import numpy as np
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i] = reversed(matrix[i])
# @lc code=end

