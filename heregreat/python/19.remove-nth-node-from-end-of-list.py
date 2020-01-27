#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur, pre= head, head
        for i in range(n):
            if(i == n-1 and cur.next == None):
                return head.next
            cur = cur.next
        while(cur.next):
            cur = cur.next
            pre = pre.next
        pre.next = pre.next.next
        return head

# @lc code=end

