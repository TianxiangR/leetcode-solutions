#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
from typing import *
import math
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        lo, hi = min(piles), max(piles)

        min_speed = hi
        while lo <= hi:
            mid = (lo + hi + 1) // 2
            min_h = 0
            for pile in piles:
                min_h += math.ceil(pile/mid)
            if min_h <= h:
                min_speed = min(min_speed, mid)
                hi = mid - 1
            else:
                lo = mid + 1
            
        return min_speed
# @lc code=end

