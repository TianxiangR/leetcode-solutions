#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        curr_queue, next_queue, level, levels = ([], [], [], [])
        curr_queue.append(root)
        level.append(root)
        levels.append(level)
        level = []
        
        while len(curr_queue):
            front: Node = curr_queue.pop(0)
            
            if front.left is not None:
                level.append(front.left)
                next_queue.append(front.left)
            if front.right is not None:
                level.append(front.right)
                next_queue.append(front.right)
                
            if len(curr_queue) == 0:
                levels.append(level)
                level = []
                curr_queue = next_queue
                next_queue = []
        
        for l in levels:
            for i in range(len(l) - 1):
                l[i].next = l[i + 1]
        
        return root
        
# @lc code=end

