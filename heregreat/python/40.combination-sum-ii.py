#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates, target: int):
        res = []
        out = []
        candidates = sorted(candidates)
        self.helper(candidates, target, 0, out, res)
        return res
        
    def helper(self, nums, target, start, out, res=[]):
            if(target == 0):
                res.append(out)
                return
            for i in range(start, len(nums)):
                if(i > start and nums[i] == nums[i-1]):
                    continue
                if(nums[i] > target):
                    break
                self.helper(nums, target - nums[i], i+1, out + [nums[i]], res)
        
# @lc code=end
data = [10,1,2,7,6,1,5]
target = 8
res = Solution().combinationSum2(data, 8)
print(res)
