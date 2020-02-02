#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if(not head):
            return None
        cur = head
        n = 1
        while(cur.next):
            n += 1
            cur = cur.next
        cur.next = head
        m = n - k % n
        for _ in range(m):
            cur = cur.next
        n_head = cur.next
        cur.next = None
        return n_head
# @lc code=end
