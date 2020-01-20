#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0 or x % 10 == 0 and x != 0):
            return False
        reverse_num = 0
        while(reverse_num < x):
            reverse_num = reverse_num * 10 + x % 10
            x = x // 10
        return reverse_num == x or reverse_num//10 == x
# @lc code=end

