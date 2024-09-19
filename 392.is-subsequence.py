#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) == 0:
            return True
        if len(t) < len(s):
            return False
        
        for j in range(len(t)):
            if t[j] == s[i]:
                i += 1
            if i == len(s):
                return True
        return False
        
        
# @lc code=end

