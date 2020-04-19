#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if(len(nums) < 3):
            return max(nums)
        for _ in range(2):
            nums.remove(max(nums))
        return max(nums)

# @lc code=end

