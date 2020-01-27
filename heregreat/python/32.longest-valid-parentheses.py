#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        start, index= 0, 0
        res = 0
        for i in s:
            index += 1
            if(i == '('):
                stack.append(index)
            elif(i == ')'):
                if(len(stack) == 0):
                    start = index
                else:
                    stack.pop()
                    if(len(stack) == 0):
                        res = max(res, index - start)
                    else:
                        res = max(res, index - stack[-1])
        return res
# @lc code=end

