#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from typing import *
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        modify_index = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[modify_index] = nums[i]
                modify_index += 1
            else:
                zeros += 1
        
        for i in range(zeros):
            nums[-1 - i] = 0
            
        
# @lc code=end

