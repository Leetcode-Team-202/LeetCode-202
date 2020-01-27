#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        res=[]
        index = -1
        nums = sorted(nums)
        if(len(nums) == 0):
            return res
        for i in nums:
            index += 1
            if(i > 0):
                break
            if(index > 0 and i == nums[index-1]):
                continue
            target = 0 - i
            j = index + 1
            k = len(nums) - 1
            while(j < k):
                if(nums[j] + nums[k] == target):
                    res.append([i, nums[j], nums[k]])
                    while(j < k and nums[j] == nums[j+1]):
                        j += 1
                    while(j < k and nums[k] == nums[k-1]):
                        k -= 1
                    k -= 1
                    j += 1
                elif(nums[j] + nums[k] > target):
                    k -= 1
                elif(nums[j] + nums[k] < target):
                    j += 1 
        return res
# @lc code=end

