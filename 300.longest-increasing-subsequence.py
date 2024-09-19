#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from typing import *
# @lc code=start
class Solution:
    def _binaryInsert(self, nums: List[int], num: int) -> None:
        if num < nums[0]:
            nums[0] = num
            return
        if num > nums[-1]:
            return
        
        start = 0
        end = len(nums)
        prev = None
        while start != end:
            mid = (end  - start) // 2
            if nums[mid - 1] == num:
                return
            if nums[mid - 1] < num <= nums[mid]:
                nums[mid] = num
                return
            if nums[mid] < num <= nums[mid + 1]:
                nums[mid + 1] = num
                return
            
            if nums[mid] > num:
                end = mid - 1
            else:
                start = mid + 1 
            
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        
        for num in nums:
            if len(tails) == 0 or tails[-1] < num:
                tails.append(num)
            else:
                self._binaryInsert(tails, num)
        
        return len(tails)
        
# @lc code=end

