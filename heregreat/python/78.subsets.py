#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums = sorted(nums)
        for i in nums:
            size = len(res)
            for j in range(0, size):
                res.append(res[j])
                new = list(res.pop())
                new.append(i)
                res.append(new)
        return res       
# @lc code=end
print(Solution().subsets([1,2,3]))