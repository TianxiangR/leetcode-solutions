#
# @lc app=leetcode id=2300 lang=python3
#
# [2300] Successful Pairs of Spells and Potions
#
from typing import *
# @lc code=start
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        output = []
        # time complexity: O(nlogm) where n == len(spells) and m == len(potions)
        for i in range(len(spells)):
            lo, hi = 0, len(potions) - 1
            smallest_valid_index = len(potions)
            if spells[i] * potions[lo] >= success:
                output.append(len(potions))
                continue
            elif spells[i] * potions[hi] < success:
                output.append(0)
                continue
            
            while lo <= hi:
                mid = (lo + hi + 1) // 2
                power = spells[i] * potions[mid]
                if power == success:
                    # it's a valid power, and we know where to stop
                    curr = potions[mid]
                    smallest_valid_index = mid
                    while smallest_valid_index > 0 and potions[smallest_valid_index - 1] == curr:
                        smallest_valid_index -= 1
                    break
                elif power < success:
                    # not valid
                    lo = mid + 1
                else:
                    # it's valid but we don't know where to stop
                    hi = mid - 1
                    smallest_valid_index = min(smallest_valid_index, mid)
            
            output.append(len(potions) - smallest_valid_index)
        
        return output
                
# @lc code=end

