#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#
from typing import *
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def _construct(self, grid: List[List[int]], top_left: tuple[int, int], bottom_right: tuple[int, int]) -> 'Node':
        top_i, top_j = top_left
        bottom_i, bottom_j = bottom_right
        
        width = bottom_i - top_i + 1
        
        if width == 1:
            return Node(grid[top_i][top_j], 1, None, None, None, None)
        
        mid_i = (bottom_i + top_i + 1) // 2
        mid_j = (bottom_j + top_j + 1) // 2 
        
        topLeft = self._construct(grid, top_left, (mid_i - 1, mid_j - 1))
        topRight = self._construct(grid, (top_i, mid_j), (mid_i - 1, bottom_j))
        bottomLeft = self._construct(grid, (mid_i, top_j), (bottom_i, mid_j - 1))
        bottomRight = self._construct(grid, (mid_i, mid_j), bottom_right)

        children = [topLeft, topRight, bottomLeft, bottomRight]
        isLeaf = True
        childSum = 0
        for child in children:
            isLeaf = isLeaf and child.isLeaf
            childSum += child.val
        
        isLeaf = isLeaf and (childSum == 0 or childSum == 4)
        
        if isLeaf:
            val = childSum // 4
            return Node(val, True, None, None, None, None)
        
        return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
               
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self._construct(grid, (0, 0), (len(grid) - 1, len(grid) - 1))
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    
    solution.construct(grid)