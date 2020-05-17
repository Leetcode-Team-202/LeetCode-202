#
# @lc app=leetcode id=553 lang=python3
#
# [553] Optimal Division
#

# @lc code=start
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        res = str(nums[0])
        if(len(nums) == 1):
            return res
        elif(len(nums) == 2):
            return res + '/' + str(nums[1])
        res += '/(' + str(nums[1])
        for i in nums[2:]:
            res += '/' + str(i)
        return res + ')'
# @lc code=end

