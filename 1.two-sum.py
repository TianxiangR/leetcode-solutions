#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import *
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in map:
                return [i, map[remainder]]
            
            map[nums[i]] = i
        
        return [-1, -1]
            
# @lc code=end

