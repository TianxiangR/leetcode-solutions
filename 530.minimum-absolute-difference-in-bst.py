#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDiff = float('inf')        
        self.helper(root)
        return self.minDiff
    
    def helper(self, root: Optional[TreeNode]) -> List[int]:
        left_val = [root.val, root.val]
        right_val = [root.val, root.val]
        
        if root.left:
            left_val = self.helper(root.left)
            self.minDiff = min(self.minDiff, root.val - left_val[1])
        if root.right:
            right_val = self.helper(root.right)
            self.minDiff = min(self.minDiff, right_val[0] - root.val)
                    
        return [left_val[0], right_val[1]]
        
        
# @lc code=end

