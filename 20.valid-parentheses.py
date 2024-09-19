#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

parenth_map = {
    "(": ")",
    "[": "]",
    "{": "}"
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for p in s:
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
            elif len(stack) > 0:
                top = stack.pop()
                if parenth_map[top] != p:
                    return False
            else:
                return False
        return len(stack) == 0
# @lc code=end

