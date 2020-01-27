#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def DFS(left, right, out, res):
            if(left < 0 or right < 0 or left > right):
                return
            if(left == 0 and right == 0):
                return res.append(out)
            DFS(left-1, right, out + '(', res)
            DFS(left, right-1, out+')', res)
        res = []
        DFS(n, n, '', res)
        return res
# @lc code=end

