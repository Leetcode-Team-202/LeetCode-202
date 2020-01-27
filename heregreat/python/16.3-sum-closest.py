#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closet = nums[0] + nums[1] + nums[2]
        diff = abs(nums[0] + nums[1] + nums[2] - target)
        index = 0
        nums = sorted(nums)
        for i in nums:
            index += 1
            j = index
            k = len(nums) - 1
            while(j < k):
                sum = i + nums[j] + nums[k]
                newdiff = abs(sum -target)
                if(diff > newdiff):
                    diff = newdiff
                    closet = sum
                if(sum < target):
                    j += 1
                else:
                    k -= 1
        return closet
# @lc code=end

