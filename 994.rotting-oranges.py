#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
from typing import *
from collections import deque
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue: deque[list[int]] = deque()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        fresh_orange_count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cell = grid[i][j]
                if cell == 1:
                    fresh_orange_count += 1
                elif cell == 2:
                    queue.append([i, j, 0])
        
        time_required = 0
        
        while len(queue):
            i, j, minutes = queue.popleft()
            
            for dir in dirs:
                next_i = i + dir[0]
                next_j = j + dir[1]
                
                time_required = max(time_required, minutes)
                
                if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]) and grid[next_i][next_j] == 1:
                    grid[next_i][next_j] = 2
                    fresh_orange_count -= 1
                    queue.append([next_i, next_j, minutes + 1])
            
        return time_required if fresh_orange_count == 0 else -1
# @lc code=end

