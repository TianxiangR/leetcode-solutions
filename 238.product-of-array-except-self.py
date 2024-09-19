#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import *
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct: list[int] = [nums[0]]
        suffixProduct: list[int] = [nums[-1]]
        
        for i in range(1, len(nums)):
            prefixProduct.append(prefixProduct[-1] * nums[i])
        
        for i in reversed(range(len(nums) - 1)):
            suffixProduct.append(suffixProduct[-1] * nums[i])
        
        suffixProduct.reverse()
        
        output = []
        
        for i in range(len(nums)):
            before = 1
            after = 1
            
            if i == 0 and i + 1 < len(nums):
                after = suffixProduct[i + 1]
            elif i == len(nums) - 1 and i - 1 >= 0:
                before = prefixProduct[i - 1]
            else:
                after = suffixProduct[i + 1]
                before = prefixProduct[i - 1]
            
            output.append(before * after)
        
        return output
        
        
# @lc code=end

