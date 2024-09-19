#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map: dict[int, 'Node'] = {}
        
        def _clone(node: Optional['Node']) -> Optional['Node']:
            if node is None:
                return node
            
            if id(node) in map:
                return map[id(node)]
            
            copy = Node(node.val)
            map[id(node)] = copy
            
            if node.neighbors is not None:
                copy.neighbors = []
                for neighbor in node.neighbors:
                    cloned_neighbor = _clone(neighbor)
                    copy.neighbors.append(cloned_neighbor)
            
            return copy
        
        return _clone(node)
            
        
# @lc code=end

