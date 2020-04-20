#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
from typing import List
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if(len(s) == 0 or len(p) > len(s)):
            return
        hash_s = {}
        hash_p = {}
        res = []
        for i in range(len(p)):
            if p[i] not in hash_p.keys():
                hash_p[p[i]] = 0
            if s[i] not in hash_s.keys():
                hash_s[s[i]] = 0
            hash_p[p[i]] += 1
            hash_s[s[i]] += 1
        if(hash_p == hash_s):
            res.append(0)
        for i in range(len(p), len(s)):
            if s[i] not in hash_s.keys():
                hash_s[s[i]] = 0
            hash_s[s[i]] += 1
            hash_s[s[i-len(p)]] -= 1
            if(hash_s[s[i-len(p)]] == 0):
                del hash_s[s[i-len(p)]]
            if(hash_p == hash_s):
                res.append(i - len(p) + 1)
        return res
# @lc code=end
print(Solution().findAnagrams("cbaebabacd", "abc"))
