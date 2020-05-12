#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#
from typing import List
# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if(len(board) == 0 or len(board[0]) == 0):
            return
        row = click[0]
        col = click[1]
        num = 0
        rec = []
        if(board[row][col] == 'M'):
            board[row][col] = 'X'
        else:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    x = row + i
                    y = col + j
                    if(x < 0 or x >= len(board) or y < 0 or y >= len(board[0])):
                        continue
                    if(board[x][y] == 'M'):
                        num += 1
                    elif(num == 0 and board[x][y] == 'E'):
                        rec.append([x,y])
            if(num > 0):
                board[row][col] = str(num)
            else:
                for i in rec:
                    board[i[0]][i[1]] = 'B'
                    self.updateBoard(board, i)
        return board
# @lc code=end
print(Solution().updateBoard([["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], [1,2]))