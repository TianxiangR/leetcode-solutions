#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from typing import *
# @lc code=start
class Solution:
    
    def _is_valid_position(self, board: List[List[str]], i: int, j: int) -> bool:
        return 0 <= i < len(board) and 0 <= j < len(board[0])
    
    def _get_neighbors(self, board: List[List[str]], i: int, j: int) -> list[tuple[int]]:
        output = []
        
        if i > 0:
            output.append((i - 1, j))
        if j > 0:
            output.append((i, j - 1))
        if i < len(board) - 1:
            output.append((i + 1, j))
        if j < len(board[0]) - 1:
            output.append((i, j + 1))
        
        return output
    
    def searchFrom(self, board: List[List[str]], word: str, i: int, j: int) -> bool:
        if word[0] == board[i][j]:
            if len(word) == 1:
                return True

            neighbors = self._get_neighbors(board, i, j)
            saved_char = board[i][j]
            board[i][j] = "#"
            for neighbor in neighbors:
                if self.searchFrom(board, word[1:], neighbor[0], neighbor[1]):
                    board[i][j] = saved_char
                    return True
                
            board[i][j] = saved_char
            return False
        
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.searchFrom(board, word, i, j):
                        return True
        
        return False
                    
        
# @lc code=end

