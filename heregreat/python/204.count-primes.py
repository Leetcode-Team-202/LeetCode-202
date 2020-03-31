#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True for _ in range(n)]
        res = 0
        for i in range(2, n):
            if( not isPrime[i]):
                continue
            res += 1
            j = 2
            while(i * j < n):
                isPrime[i*j] = False
                j += 1
        return res
# @lc code=end

