#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
from typing import List
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        out = []
        self.helper(1, n, k, res, out)
        return res
    def helper(self, start, n, k, res, out):
        if(len(out) == k):
            res.append(out[:])
            return
        for i in range(start, n + 1):
            out.append(i)
            self.helper(i+1, n, k, res, out)
            out.pop()
# @lc code=end
print(Solution().combine(4,2))