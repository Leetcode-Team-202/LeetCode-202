#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
class Solution:
    def take_second(self, elem):
        return elem[1]
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pair = sorted(pairs, key = self.take_second)
        cur, res= pair[0][0] - 1, 0
        for x, y in pair:
            if cur < x:
                cur = y
                res += 1
        return res
        
# @lc code=end

