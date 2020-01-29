#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, 0, res)
        return res
    def helper(self, nums=[], start=0, res=[]):
        if(start >= len(nums)):
            res.append(nums[:])
        for i in range(start, len(nums)):
            self.swap(nums, start, i)
            self.helper(nums, start + 1, res)
            self.swap(nums, start, i)
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        return nums
# @lc code=end
print(Solution().permute([1,2,3]))
