#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if(root == None):
            return True
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, root, left, right):
        if(root == None):
            return True    
        val = root.val
        if val <= left or val >= right:
                return False   
        return self.helper(root.right, val, right) and self.helper(root.left, left, val)
    
# @lc code=end

