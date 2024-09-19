#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
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
    MIN_VAL = int(-1e4) - 1      
    def _goodNodes(self, node: Optional[TreeNode], currMax=MIN_VAL) -> int:
        if node is None:
            return 0
        
        currMax = max(currMax, node.val)
        
        left_count = self._goodNodes(node.left, currMax)
        right_count = self._goodNodes(node.right, currMax)
        
        return left_count + right_count + int(node.val >= currMax)
        
        
    def goodNodes(self, root: TreeNode) -> int:
        return self._goodNodes(root)
        
# @lc code=end

