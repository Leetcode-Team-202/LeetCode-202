#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#
from typing import List
# @lc code=start
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        sum, index, F = 0, 0, 0
        for i in A:
            sum += i
            F += index * i
            index += 1
        res = F
        for i in range(1, len(A)):
            F = F + sum - len(A) * A[len(A) - i]
            res = max(F, res)
        return res
# @lc code=end

print(Solution().maxRotateFunction([4,3,2,6]))
