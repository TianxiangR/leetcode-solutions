#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
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
    def _pathSum(self, root: Optional[TreeNode], targetSum: int, prefixSum = [0]) -> int:
        if root is None:
            return 0
        
        prefixSum.append(prefixSum[-1] + root.val)
        
        curr_count = 0
        for i in range(len(prefixSum) - 1):
            sub_sum = prefixSum[i]
            if prefixSum[-1] - sub_sum == targetSum:
                curr_count += 1
        
        left_count = self._pathSum(root.left, targetSum, prefixSum)
        right_count = self._pathSum(root.right, targetSum, prefixSum)
        
        prefixSum.pop()
        
        return curr_count + left_count + right_count
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self._pathSum(root, targetSum)
        
# @lc code=end

