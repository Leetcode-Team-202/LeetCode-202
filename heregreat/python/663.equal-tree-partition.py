#
# @lc app=leetcode id=663 lang=python3
#
# [663] Equal Tree Partition
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        seen = []
    
        def coll_sum(node):
            if not node:
                return 0
            seen.append(coll_sum(node.left) + node.val + coll_sum(node.right))
            return seen[-1]
        
        total = coll_sum(root)
        seen.pop()
        return total/2 in seen
# @lc code=end

