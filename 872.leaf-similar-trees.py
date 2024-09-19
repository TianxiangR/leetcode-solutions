#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
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
    def _isLeaf(self, node: Optional[TreeNode]) -> bool:
        if node is None:
            return False
        
        return node.left is None and node.right is None
    
    def _getLeaves(self, root: Optional[TreeNode]) -> list[TreeNode]:
        if root is None:
            return []
        
        if self._isLeaf(root):
            return [root]
        
        left_leaves = self._getLeaves(root.left)
        right_leaves = self._getLeaves(root.right)
        
        return left_leaves + right_leaves
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_leaves = self._getLeaves(root1)
        root2_leaves = self._getLeaves(root2)
        
        if len(root1_leaves) != len(root2_leaves):
            return False
        
        for i in range(len(root1_leaves)):
            if root1_leaves[i].val != root2_leaves[i].val:
                return False
        
        return True
        
# @lc code=end

