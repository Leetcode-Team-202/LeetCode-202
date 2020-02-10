#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if(len(matrix) == 0 or len(matrix[0]) == 0):
            return False
        left, right= 0, len(matrix)
        while(left < right):
            mid = left + (right - left)//2
            if(matrix[mid][0] < target):
                left = mid + 1
            elif(matrix[mid][0] == target):
                return True
            else:
                right = mid
        if(right > 0):
            row = right - 1
        else:
            row = right
        left, right = 0, len(matrix[row])
        while(left < right):
            mid = left + (right - left)//2
            if(matrix[row][mid] == target):
                return True
            elif(matrix[row][mid] < target):
                left = mid + 1
            else:
                right = mid
        return False
         
# @lc code=end

