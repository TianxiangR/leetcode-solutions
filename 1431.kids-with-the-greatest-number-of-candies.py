#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#
from typing import *
# @lc code=start


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        output = []
        
        for candy in candies:
            output.append(candy + extraCandies >= maxCandies)
            
        return output
# @lc code=end

