#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if(len(board) == 0 or len(board[0]) == 0):
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(self.DFS(board, word, 0, i, j)):
                    return True
        return False
    def DFS(self, board, word, idx, i, j):
        if(idx == len(word)):
            return True
        if(i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[idx]):
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        res = self.DFS(board, word, idx + 1, i - 1, j) or self.DFS(board, word, idx + 1, i + 1, j) or self.DFS(board, word, idx + 1, i, j - 1) or self.DFS(board, word, idx + 1, i, j + 1)
        board[i][j] = tmp
        return res

# @lc code=end

