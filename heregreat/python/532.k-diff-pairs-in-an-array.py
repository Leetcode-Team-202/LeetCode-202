#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = {}
        res = 0
        for i in nums:
            if(i not in dic.keys()):
                dic[i] = 0
            dic[i] += 1
        for i in dic:
            if(k == 0 and dic[i] > 1):
                res += 1
            elif(k > 0 and (i + k) in dic.keys()):
                res += 1
        return res

# @lc code=end

