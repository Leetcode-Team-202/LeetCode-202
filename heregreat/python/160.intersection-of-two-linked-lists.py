#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if(headA == None or headB == None):
            return None
        a, b = headA, headB
        while(a != b):
            if(a == None):
                a = headB
            else:
                a = a.next
            if(b == None):
                b = headA
            else:
                b = b.next
        return a
# @lc code=end

