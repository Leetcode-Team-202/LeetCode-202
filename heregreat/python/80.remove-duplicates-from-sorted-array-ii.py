#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        index = i = 0
        while(index < len(nums)):
            if(i > 1 and nums[i] == nums[i - 2]):
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j+1]
                i -= 1
            else:
                count += 1
            index += 1
            i += 1
        return count
# @lc code=end
print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))
