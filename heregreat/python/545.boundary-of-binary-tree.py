#
# @lc app=leetcode id=545 lang=python3
#
# [545] Boundary of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if(not root):
            return
        if(root.left or root.right):
            self.res.append(root.val)
        
        self.leftBoundary(root.left)
        self.leaves(root)
        self.rightBoundary(root.right)
        
        return self.res
    def leftBoundary(self, root):
        if(root == None or root.left == None and root.right == None):
            return
        self.res.append(root.val)
        if(root.left == None):
            self.leftBoundary(root.right)
        else:
            self.leftBoundary(root.left)
        return
    def rightBoundary(self, root):
        if(root == None or root.left == None and root.right == None):
            return
        if(root.right == None):
            self.rightBoundary(root.left)
        else:
            self.rightBoundary(root.right)
        self.res.append(root.val)
        return

    def leaves(self, root):
        if(not root):
            return
        if(root.left == None and root.right == None):
            self.res.append(root.val)
        self.leaves(root.left)
        self.leaves(root.right)
        return
# @lc code=end

