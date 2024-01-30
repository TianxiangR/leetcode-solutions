#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        
        if len(new_str) == 0:
            return True
        
        p = 0
        q = len(new_str) - 1
        
        while p < q:
            if new_str[p] != new_str[q]:
                return False
            p += 1
            q -= 1
        
        return True
        
        
# @lc code=end

