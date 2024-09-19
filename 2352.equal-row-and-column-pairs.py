#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#
from typing import *
import collections
# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:        
        row_counter = collections.Counter(tuple(row) for row in grid)
        
        output = 0
        for i in range(len(grid[0])):
            col = [grid[j][i] for j in range(len(grid))]
            output += row_counter.get(tuple(col), 0)
        
        return output
                
# @lc code=end

