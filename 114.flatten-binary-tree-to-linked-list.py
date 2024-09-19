#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
from typing import Optional
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

def isLeaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None

def dfs(root: Optional[TreeNode]) -> [TreeNode, TreeNode]:
    if root is None or isLeaf(root):
        return [root, root]
    
    curr_tail = root
    original_left = root.left
    original_right = root.right
    
    if original_left is not None:
        left_list = dfs(original_left)
        curr_tail.right = left_list[0]
        curr_tail = left_list[1]
    
    if original_right is not None:
        right_list = dfs(original_right)
        curr_tail.right = right_list[0]
        curr_tail = right_list[1]
    
    return [root, curr_tail]


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        dfs(root)
        return
        
# @lc code=end

