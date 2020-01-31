#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0 for _ in nums]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i - 1], nums[i - 1]) - 1
            if(dp[i] < 0):
                return False
        return True
            
# @lc code=end

