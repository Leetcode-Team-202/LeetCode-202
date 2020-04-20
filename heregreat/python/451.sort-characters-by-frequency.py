#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
from queue import PriorityQueue
class Solution:
    def frequencySort(self, s: str) -> str:
        q = PriorityQueue()
        m = {}
        res = []
        for i in s:
            if i not in m.keys():
                m[i] = 0
            m[i] += 1
        for i in m.keys():
            q.put((m[i], i))
        
        while not q.empty():
            f, s = q.get()
            for _ in range(f):
                res.append(s)
        res = reversed(res)
        return "".join(res)
# @lc code=end
print(Solution().frequencySort("tree"))
