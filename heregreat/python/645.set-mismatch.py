#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if(nums[i] == nums[i-1]):
                dupli = nums[i]
            if(nums[i] > nums[i-1] + 1):
                missing = nums[i-1] + 1
        if(nums[-1] != len(nums)):
            missing = len(nums)
        if(nums[0] != 1):
            missing = 1
        return[dupli, missing]
# @lc code=end

