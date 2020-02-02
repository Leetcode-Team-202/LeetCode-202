#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        nums = [i for i in range(1, n+1)]
        for i in range(n , 0, -1):
            index = (k - 1) // self.fact(i - 1)
            k = k % self.fact(i - 1)
            res += str(nums[index])
            nums.pop(index)
        return res
    def fact(self, n):
        res = 1
        for i in range(n, 0, -1):
            res = res * i
        return res
# @lc code=end
print(Solution().getPermutation(3, 3))
