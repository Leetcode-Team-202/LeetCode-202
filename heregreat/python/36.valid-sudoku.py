#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board) -> bool:
        row = 0
        st = set()
        for i in board:
            colume = 0
            row += 1
            for j in i:
                colume += 1
                if(j=='.'):
                    continue
                t = '(' + j + ')'
                row_ = str(row) + t
                colume_ = t + str(colume)
                sub = str((row-1)//3) + t + str((colume-1)//3)
                if((row_ in st) or (colume_ in st) or (sub in st) ):
                    return False
                st.add(row_)
                st.add(colume_)
                st.add(sub)
        return True
# @lc code=end
data = [
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]
res = Solution().isValidSudoku(data)
print(res)