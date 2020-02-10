#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
from typing import List
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = [0, 0, 0]
        for i in nums:
            if(i == 0):
                index[0] += 1
            elif(i == 1):
                index[1] += 1
            else:
                index[2] += 1
        first = index[0]
        second = index[0] + index[1]
        for i in range(len(nums)):
            if(i < first):
                nums[i] = 0
            elif(i < second):
                nums[i] = 1
            else:
                nums[i] = 2
# @lc code=end
print(Solution().sortColors([2,0,2,1,1,0]))
