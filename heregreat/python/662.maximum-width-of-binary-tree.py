#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = [(root, 0, 0)]
        res = curdepth = left = 0 
        for node, depth, pos in queue:
            if(node):
                queue.append((node.left, depth+1, pos*2))
                queue.append((node.right, depth+1, pos*2+1))
                if(curdepth != depth):
                    curdepth = depth
                    left = pos
                res = max(res, pos-left+1)
        return res
# @lc code=end

