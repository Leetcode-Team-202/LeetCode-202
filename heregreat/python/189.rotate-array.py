#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, k = len(nums), k%len(nums)
        if(n == 0 or k == 0):
            return
        self.reverse(nums, 0, n-k-1)
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-1)
    def reverse(self, nums, l, r):
        while(l < r):
            tem = nums[l]
            nums[l] = nums[r]
            nums[r] = tem
            l += 1
            r -= 1 
# @lc code=end

