#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
from typing import *

# @lc code=start
from collections import deque
import sys
class Solution:
    def _dfs(self, board: List[List[str]], i: int, j: int) -> None:
        if board[i][j] == "X":
            return
        
        queue: deque[tuple[int, int]] = deque()
        
        neighbors: list[tuple[int, int]] = []
        if i > 0 and board[i - 1][j] == "O":
            neighbors.append((i - 1, j))
        if i < len(board) - 1 and board[i + 1][j] == "O":
            neighbors.append((i + 1, j))
        if j > 0 and board[i][j - 1] == "O":
            neighbors.append((i, j - 1))
        if j < len(board[0]) - 1 and board[i][j + 1] == "O":
            neighbors.append((i, j + 1))
        
        board[i][j] = "#"
        for a, b in neighbors:
            self._dfs(board, a, b)
                
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dimension = len(board) * len(board[0])
        
        sys.setrecursionlimit(max(1000, dimension + 1))
        for i in range(len(board)):
            self._dfs(board, i, 0)
            self._dfs(board, i, len(board[0]) - 1)
        
        for j in range(len(board[0])):
            self._dfs(board, 0, j)
            self._dfs(board, len(board) - 1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                if c == "O":
                    board[i][j] = "X"
                elif c == "#":
                    board[i][j] = "O"
# @lc code=end
if __name__ == "__main__":
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    solution = Solution()
    
    solution.solve(board)

