#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            new = "".join(sorted(i))
            if(new not in dic.keys()):
                dic[new] = [i]
            else:
                dic[new].append(i)
        return list(dic.values())
   
# @lc code=end
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
