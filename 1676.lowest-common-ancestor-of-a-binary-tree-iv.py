from typing import *
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    class State:
      BOTH_PENDING = 0
      LEFT_DONE = 1
      BOTH_DONE = 2
  
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        targets = set([node.val for node in nodes])
        remaining = len(nodes)
        
        stack: list[tuple['TreeNode', int, int]] = [(root, self.State.BOTH_PENDING, 0)]
        
        lca = root
        lca_level = 0
        while len(stack):
          node, state, level = stack.pop()
          
          if state == self.State.BOTH_PENDING and node.val in targets:
            if remaining == len(nodes):
              lca = node
              lca_level = level
              
            remaining -= 1
            
            if remaining == 0:
              return lca
          
          if state == self.State.BOTH_PENDING:
            stack.append((node, state + 1, level))
            if node.left:
              stack.append((node.left, self.State.BOTH_PENDING, level + 1))
          elif state == self.State.LEFT_DONE:
            stack.append((node, state + 1, level))
            if node.right:
              stack.append((node.right, self.State.BOTH_PENDING, level + 1))
          else:
            if level - 1 < lca_level:
              lca_level = level - 1
              lca = stack[-1][0]
        
        return lca