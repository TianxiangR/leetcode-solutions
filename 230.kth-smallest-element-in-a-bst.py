#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
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
    class State:
        BOTH_NOT_DONE = 0
        LEFT_DONE = 1
        BOTH_DONE = 2
        
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        found_smallest: bool = False
        kth: int = 0
        kth_smallest: int = root.val
        
        stack: list[tuple[TreeNode, int]] = [(root, self.State.BOTH_NOT_DONE)]
        
        while True:
            node, state = stack.pop()
            if node.left is None and node.right is None:
                if not found_smallest:
                    found_smallest = True
                    kth = 1
                else:
                    kth += 1
                state = self.State.BOTH_DONE
                            
            if state == self.State.BOTH_NOT_DONE:
                stack.append((node, self.State.LEFT_DONE))
                if node.left is not None:
                    stack.append((node.left, self.State.BOTH_NOT_DONE))
            elif state == self.State.LEFT_DONE:
                stack.append((node, self.State.BOTH_DONE))
                if node.right is not None:
                    stack.append((node.right, self.State.BOTH_NOT_DONE))
                if not found_smallest:
                    found_smallest = True
                    kth = 1
                else:
                    kth += 1
                
            
            if kth == k:
                return node.val
        
        return -1
                    
            
        
# @lc code=end

