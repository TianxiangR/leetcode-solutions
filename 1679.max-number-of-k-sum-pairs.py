#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#
from typing import *
# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        p = 0
        q = len(nums) - 1
        
        output = 0
        while p < q:
            _sum = nums[p] + nums[q]
            if _sum == k:
                output += 1
                p += 1
                q -= 1
            elif _sum < k:
                p += 1
            else:
                q -= 1
        
        return output
        
# @lc code=end

