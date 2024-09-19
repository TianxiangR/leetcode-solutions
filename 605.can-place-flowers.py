#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
from typing import *
# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                # skip
                i += 2
                continue
            
            if i == len(flowerbed) - 1 or (i + 1 < len(flowerbed) and flowerbed[i + 1] != 1):
                n -= 1
                i += 2
                continue
            
            i += 1
        
        return n <= 0
            
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    solution.canPlaceFlowers([1,0,0,0,1,0,0], 2)