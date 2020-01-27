#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def helper(y, x = 0):
            while(x < y):
                base_sum = nums[x] + nums[y]
                low, high = x + 1, y - 1
                while(low < high):
                    sum = base_sum + nums[low] + nums[high]
                    if(sum == target):
                        res.add((nums[x], nums[y], nums[low], nums[high]))
                        low += 1
                    elif(sum > target):
                        high -= 1
                    elif(sum < target):
                        low += 1
                x += 1
        
        res = set()
        nums.sort()
        for y in range(len(nums)-1, 0, -1):
            helper(y)
        return [list(x) for x in res]
# @lc code=end

