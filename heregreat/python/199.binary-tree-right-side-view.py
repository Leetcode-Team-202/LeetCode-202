#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

from typing import List
# @lc code=start
# Definition for a binary tree node.
import queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if(root == None):
            return 
        res = []
        q = queue.Queue()
        q.put(root)
        while(not q.empty()):
            layer_size = q.qsize()
            for i in range(layer_size):
                cur = q.get()
                if(cur.left):
                    q.put(cur.left)
                if(cur.right):
                    q.put(cur.right)
                if(i == layer_size - 1):
                    res.append(cur.val)
        return res


# @lc code=end

