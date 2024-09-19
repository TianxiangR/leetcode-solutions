#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
from typing import *
class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
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
    def _rightSideView(self, root: Optional[TreeNode], view: list[int], level: int=0) -> None:
        if root is None:
            return
        
        level += 1
        if len(view) < level:
            view.append(root.val)
        
        if root.right:
            self._rightSideView(root.right, view, level)
        if root.left:
            self._rightSideView(root.left, view, level)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        self._rightSideView(root, view)
        return view
        
# @lc code=end

