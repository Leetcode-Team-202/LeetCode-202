#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(len(matrix) == 0 or len(matrix[0]) == 0):
            return False
        if(target < matrix[0][0] or target > matrix[-1][-1]):
            return False
        r = len(matrix) - 1; c = 0
        while True:
            if(matrix[r][c] > target):
                r -= 1
            elif(matrix[r][c] < target):
                c += 1
            else:
                return True
            if(r < 0 or c >= len(matrix[0])):
                break
        return False
# @lc code=end

