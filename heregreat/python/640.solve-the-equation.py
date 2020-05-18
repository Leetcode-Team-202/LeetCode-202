#
# @lc app=leetcode id=640 lang=python3
#
# [640] Solve the Equation
#

# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        hs = equation.split('=')
        lhs, rhs = 0, 0
        for i in self.breakit(hs[0]):
            if('x' in i):
                lhs += int(self.coeff(i))
            else:
                rhs -= int(i)
        for i in self.breakit(hs[1]):
            if('x' in i):
                lhs -= int(self.coeff(i))
            else:
                rhs += int(i)
        if(lhs == 0 and rhs == 0):
            return "Infinite solutions"
        elif(lhs == 0 and rhs != 0):
            return "No solution"
        else:
            return 'x=' + str(int(rhs / lhs))
        
    def coeff(self, x):
        if(x == 'x'):
            return '1'
        elif(x == '-x'):
            return '-1'
        x = x.replace('x', '')
        return x
    
    def breakit(self, s):
        res = []
        r = ''
        for i in s:
            if(i == '+' or i == '-'):
                if(len(r) > 0):
                    res.append(r)
                    if(i == '-'):
                        r = '-'
                    else:
                        r = ''
                else:
                    r +=  i
            else:
                r += i
        res.append(r)
        return res
# @lc code=end

