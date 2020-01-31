#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals) == 0):
            return 
        intervals = sorted(intervals)
        res = [intervals[0]]
        for i in intervals[1:]:
            if(i[0] <= res[-1][1]):
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res
# @lc code=end

