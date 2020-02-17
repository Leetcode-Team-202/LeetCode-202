#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if(root == None):
            return
        q = Queue(0)
        q.put(root)
        res = []
        while(not q.empty()):
            onelevel = []
            for i in range(q.qsize()):
                a = q.get()
                onelevel.append(a.val)
                if(a.left != None):
                    q.put(a.left)
                if(a.right != None):
                    q.put(a.right)
            res.append(onelevel)
        return res
# @lc code=end

