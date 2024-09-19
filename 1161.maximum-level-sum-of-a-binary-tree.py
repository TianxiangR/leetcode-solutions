#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
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
    def _maxLevelSum(self, root: Optional[TreeNode], levelSum: dict, prevLevel: int=0) -> None:
        if root is None:
            return
        
        currLevel = prevLevel + 1
        levelSum[currLevel] = levelSum.get(currLevel, 0) + root.val
        
        self._maxLevelSum(root.left, levelSum, currLevel)
        self._maxLevelSum(root.right, levelSum, currLevel)
        
        return
    
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSum = {}
        
        self._maxLevelSum(root, levelSum)
        
        max_sum = float('-inf')
        max_level = 0
        for level, _sum in levelSum.items():
            if _sum > max_sum:
                max_sum = _sum
                max_level = level
            elif _sum == max_sum and level < max_level:
                max_level = level
        
        return max_level
                    
        
# @lc code=end

