#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#
from typing import *
# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        
        for num in arr:
            map[num] = map.get(num, 0) + 1
        
        seen = set()
        
        for count in map.values():
            if count in seen:
                return False
            seen.add(count)
        
        return True
# @lc code=end

