#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        subpath = path.split('/')
        stack = []
        for i in subpath:
            if(i in ['', '.']):
                continue
            elif(i == '..'):
                if(len(stack) != 0):
                    stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)
# @lc code=end

