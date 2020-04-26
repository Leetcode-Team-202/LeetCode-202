#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        res = []
        m = {}
        self.cnt = 0
        self.preorder(root, res, m)
        return res
    def preorder(self, root, res, m):
        if not root:
            return 0
        left = self.preorder(root.left, res, m)
        right = self.preorder(root.right, res, m)
        sum = left + right + root.val
        if(sum not in m.keys()):
            m[sum] = 0
        m[sum] += 1
        if(m[sum] >= self.cnt):           
            if(m[sum] > self.cnt):
                res.clear()
            res.append(sum)
            self.cnt = m[sum]
        return sum 

# @lc code=end

