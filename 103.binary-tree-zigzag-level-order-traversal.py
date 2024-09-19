#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
        PENDING = 0
        LEFT_DONE = 1
        BOTH_DONE = 2
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        depth = 0
        map = {}
        stack = [(root, self.State.PENDING)]
        
        if root is None:
            return []

        while len(stack):
            curr_node, state = stack.pop()
            
            if state == self.State.PENDING:
                if depth in map:
                    map[depth].append(curr_node.val)
                else:
                    map[depth] = [curr_node.val]
                
                if curr_node.left:
                    stack.append((curr_node, self.State.LEFT_DONE))
                    stack.append((curr_node.left, self.State.PENDING))
                    depth += 1
                else:
                    stack.append((curr_node, self.State.LEFT_DONE))
            elif state == self.State.LEFT_DONE:
                stack.append((curr_node, self.State.BOTH_DONE))
                if curr_node.right:
                    stack.append((curr_node.right, self.State.PENDING))
                    depth += 1
            else:
                depth -= 1             
            
        output = []
        reverse = False
        for _, value in map.items():
            if reverse:
                value.reverse()
                output.append(value)
            else:
                output.append(value)
            reverse = not reverse
            
        return output
# @lc code=end

