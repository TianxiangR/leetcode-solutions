#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def _maxDepth(self, root: Optional[TreeNode], currDepth: int = 0) -> int:
        if root is None:
            return currDepth
        currDepth += 1
        left_depth = self._maxDepth(root.left, currDepth)
        right_depth = self._maxDepth(root.right, currDepth)
        
        return max(currDepth, left_depth, right_depth)

    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._maxDepth(root)
        
# @lc code=end

