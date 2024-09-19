#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
from typing import *
# @lc code=start
class Solution:
    def _isPeak(nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True
        if k == 0:
            return nums[1] < nums[0]
        if k == len(nums) - 1:
            return nums[k - 1] < nums[k]

        return nums[k - 1] < nums[k] > nums[k + 1]
    
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi + 1) // 2
            if self._isPeak(nums, mid):
                return mid
            if mid > 0 and nums[mid - 1] > nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
            
        return -1
        
# @lc code=end

