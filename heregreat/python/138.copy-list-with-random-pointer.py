#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# Definition for a Node.

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        copies = {None : None}
        help = head
        while help:
            for node in [help, help.next, help.random]:
                if node not in copies:
                    copies[node] = Node(node.val)
            copies[help].next = copies[help.next]
            copies[help].random = copies[help.random]

            help = help.next
        return copies[head]
# @lc code=end

