#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import *
# @lc code=start

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dup: tuple[set[tuple[int, int, int]], set[int]] = set(), set()
        
        for i, i_val in enumerate(nums):
            if i_val in dup:
                continue
            seen = set()
            for j_val in nums[i + 1:]:
                complement = -i_val - j_val
                if complement in seen:
                    res.add(tuple(sorted([i_val, j_val, complement])))
                seen.add(j_val)
            dup.add(i_val)
        
        return [list(tp) for tp in res]
        
# @lc code=end

