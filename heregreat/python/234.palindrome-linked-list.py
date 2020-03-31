#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if(not head or not head.next):
            return True
        slow = fast = head
        st = [head.val]
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            st.append(slow.val)

        if(fast.next == None):
            st.pop()
        while(slow.next):
            slow = slow.next
            tem = st.pop()
            if(tem != slow.val):
                return False
        return True
# @lc code=end

