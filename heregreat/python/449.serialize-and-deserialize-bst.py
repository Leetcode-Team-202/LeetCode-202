#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
# Definition for a binary tree node.

from collections import *

class Codec:
    def preorder(self, root, res):
        if not root:
            res.append("#")
            return
        res.append(str(root.val))

        self.preorder(root.left, res)
        self.preorder(root.right, res)
        return

    def serialize(self, root):
        """Encodes a tree to a single string.
        """
        res = []
        self.preorder(root, res)
        return ",".join(res)
    
    def buildTree(self, q):
        nodeStr = q.popleft()
        if(nodeStr == '#'):
            return None
        newNode = TreeNode(int(nodeStr))
        newNode.left = self.buildTree(q)
        newNode.right = self.buildTree(q)

        return newNode
    
    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        """
        treeData = data.split(',')
        queue = deque(treeData)
        return self.buildTree(queue)

# Your Codec object will be instantiated and called as such:
# @lc code=end

