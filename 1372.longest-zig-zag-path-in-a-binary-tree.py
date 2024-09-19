#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    class Direction:
        LEFT = 0
        RIGHT = 1
    
    def _longestZigZagNodes(self, root: Optional[TreeNode], prevDirect: int, prevLength: int = 0) -> int:
        if root is None:
            return prevLength
        
        currLength = prevLength + 1
        next_direction = (prevDirect + 1) % 2
        left_length = self._longestZigZagNodes(root.left, self.Direction.LEFT, 1 if next_direction != self.Direction.LEFT else currLength)
        right_length = self._longestZigZagNodes(root.right, self.Direction.RIGHT, 1 if next_direction != self.Direction.RIGHT else currLength)
        
        return max(left_length, right_length)
        
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self._longestZigZagNodes(root, self.Direction.LEFT), self._longestZigZagNodes(root, self.Direction.RIGHT)) - 1
        
# @lc code=end
