#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
from typing import List
# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] + (1<<i))
        return res
# @lc code=end
print(Solution().grayCode(2))
