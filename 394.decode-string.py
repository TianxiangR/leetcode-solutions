#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        k_stack: list[int] = []
        str_stack: list[str] = [""]
        
        num_str = ""
        for c in s:
            if c.isnumeric():
                num_str += c
            elif c == "[":
                k_stack.append(int(num_str))
                num_str = ""
                str_stack.append("")
            elif c.isalpha():
                str_stack[-1] += c
            else:
                string = str_stack.pop()
                k = k_stack.pop()
                str_stack[-1] += string * k
        
        return str_stack[-1]
        
# @lc code=end

