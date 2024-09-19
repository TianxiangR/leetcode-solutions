#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        counter = 0
        seen = set()
        
        for c in s:
            if c in seen:
                counter += 1
                seen = set()
            seen.add(c)
        
        return counter + int(len(seen) > 0)
        
# @lc code=end

