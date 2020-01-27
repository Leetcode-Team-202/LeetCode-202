#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        res = []
        for i in digits:
            tmp = []
            for j in dic[i]:
                if len(res) == 0:
                    tmp.append(j)
                else:
                    for k in res:
                        k = k + j
                        tmp.append(k)
            res = tmp
        return res
# @lc code=end

