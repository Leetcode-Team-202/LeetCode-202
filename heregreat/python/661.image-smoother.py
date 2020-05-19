#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#
# @lc code=start
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        R, C = len(M), len(M[0])
        res = [[0] * C for _ in M]
        for r in range(R):
            for c in range(C):
                count = 0
                for i in [r-1, r, r+1]:
                    for j in [c-1, c, c+1]:
                        if(0<=i<R and 0<=j<C):
                            res[r][c] += M[i][j]
                            count += 1
                res[r][c] //= count
        return res
# @lc code=end

