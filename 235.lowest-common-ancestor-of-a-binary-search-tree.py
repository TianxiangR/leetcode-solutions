#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        return "<TreeNode: " + str(self.val) + ">"

class Solution:
    PENDING = 2
    ONE_DONE = 1
    BOTH_DONE = 0
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = 0
        found = 0
        depth = 0
        smaller_val = min(p.val, q.val)
        larger_val = max(p.val ,q.val)
        current_seach_val = smaller_val
        
        stack = [(root, Solution.PENDING)]
        
        while len(stack):
            node, state = stack.pop()
            if found == 1:
                lca = min(lca, depth)
            
            if state == Solution.PENDING:
                stack.append((node, Solution.ONE_DONE))
            elif state == Solution.ONE_DONE:
                stack.append((node, Solution.BOTH_DONE))
            else:
                depth -= 1
                continue
            if node.val == current_seach_val:
                found += 1
                if found == 2:
                    return stack[lca][0]
                else:
                    lca = depth
                    current_seach_val = larger_val

            if node.val > current_seach_val and node.left:
                stack.append((node.left, Solution.PENDING))
                depth += 1
            elif node.val < current_seach_val and node.right:
                stack.append((node.right, Solution.PENDING))
                depth += 1                       
            
        return None
# @lc code=end

