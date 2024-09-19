#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#
from typing import *
# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        _sum = 0
        max_sum = _sum
        for num in gain:
            _sum += num
            max_sum = max(max_sum, _sum)
        
        return max_sum
        
# @lc code=end

