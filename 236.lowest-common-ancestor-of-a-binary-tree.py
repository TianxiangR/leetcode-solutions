#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "<TreeNode: " + str(self.val) + ">"
# @lc code=start
# Definition for a binary tree node.
class Solution:
    class State:
        BOTH_PENDING = 0
        LEFT_DONE = 1
        BOTH_DONE = 2
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # list[tuple[TreeNode, State]]
        stack: list[tuple[TreeNode, int]] = [(root, self.State.BOTH_PENDING, 1)]
        lca = None
        lca_level = 0
        found_one = False
        
        while len(stack):
            node, state, level = stack.pop()            
            if node is None:
                continue
            
            if (node.val == p.val or node.val == q.val) and lca != node:
                if not found_one:
                    found_one = True
                    lca = node
                    lca_level = level
                else:
                    return lca
            
            if state == self.State.BOTH_PENDING:
                stack.append((node, state + 1, level))
                stack.append((node.left, state, level + 1))  
            elif state == self.State.LEFT_DONE:
                stack.append((node, state + 1, level))
                stack.append((node.right, state - 1, level + 1))
            else:
                if level - 1 < lca_level:
                    lca = stack[-1][0]
                    lca_level = level - 1
            
        return lca or root
            
# @lc code=end

if __name__ == "__main__":
    left = TreeNode(7)
    right = TreeNode(4)
    temp = TreeNode(2)
    temp.left = left
    temp.right = right
    right = temp
    left = TreeNode(6)
    temp = TreeNode(5)
    temp.left = left
    temp.right = right
    left = temp
    root = TreeNode(3)
    root.left = left

    left = TreeNode(0)
    right = TreeNode(8)
    temp = TreeNode(1)
    temp.left = left
    temp.right = right
    right = temp
    root.right = right
    
    # right = TreeNode(2)
    # root = TreeNode(1)
    # root.right = right
    
    # right = TreeNode(4)
    # left = TreeNode(2)
    # left.right = right
    # right = TreeNode(3)
    # root = TreeNode(1)
    # root.left = left
    # root.right = right
    
    s = Solution()
    print(s.lowestCommonAncestor(root, TreeNode(5), TreeNode(4)))
    
    
    
    

