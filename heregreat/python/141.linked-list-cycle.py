#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pre, las = head, head
        while(pre != None and pre.next != None):
            pre, las = pre.next.next, las.next
            if(pre == las):
                return True
        return False

# @lc code=end

