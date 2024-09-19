#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
from typing import *
# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        
        increasingSequance = [nums[0]]
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > increasingSequance[-1]:
                increasingSequance.append(nums[i])
            else:
                if len(increasingSequance) == 2:
                    if increasingSequance[0] < nums[i] < increasingSequance[1]:
                        increasingSequance[1] = nums[i]
                    elif nums[i] < increasingSequance[0]:
                        increasingSequance[0] = nums[i]
                else:
                    increasingSequance[-1] = min(increasingSequance[-1], nums[i])
            prev = nums[i]
            
            if len(increasingSequance) == 3:
                return True
        
        return False
        
        
        
# @lc code=end

