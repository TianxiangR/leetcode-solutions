#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:        
        curr = root
        prev = None
        while curr is not None:
            if curr.val == key:
                break
            prev = curr
            if curr.val > key:
                curr = curr.left
            else:
                curr = curr.right
        
        replace_node = None
        
        if curr is None:
            # not found
            return root
        
        if curr.right is not None:
            replace_node = curr.right
            left_leaf: TreeNode = replace_node
            
            while left_leaf.left is not None:
                left_leaf = left_leaf.left
            
            left_leaf.left = curr.left
        elif curr.left is not None:
            replace_node = curr.left

        if prev is not None:
            if curr.val < prev.val:
                prev.left = replace_node
            else:
                prev.right = replace_node
        else:
            root = replace_node
        
        return root
                
# @lc code=end

