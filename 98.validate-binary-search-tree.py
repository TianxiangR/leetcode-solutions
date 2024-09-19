#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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
INT_MAX = 2147483648
INT_MIN = -9223372036854775809
class Solution:
    def isValid(self, root: Optional[TreeNode], lt: int, gt: int) -> bool:
        if root is None:
            return True
        
        if root.val >= lt or root.val <= gt:
            return False
        
        left_valid = self.isValid(root.left, root.val, gt)
        right_valid = self.isValid(root.right, lt, root.val)
        
        return left_valid and right_valid
            
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, INT_MAX, INT_MIN)
        
        
# @lc code=end

