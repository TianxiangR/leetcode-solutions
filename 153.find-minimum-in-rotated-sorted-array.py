#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
from typing import *
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        p , q = 0, len(nums) - 1
        
        while p < q:
            mid = (p + q + 1) // 2
            if (mid == 0 or nums[mid - 1] > nums[mid]) and (mid == len(nums) - 1 or nums[mid + 1] > nums[mid]):
                return nums[mid]
            
            if (mid == 0 or nums[mid - 1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid + 1] < nums[mid]):
                return nums[mid + 1] if mid < len(nums) - 1 else nums[0]
            
            if nums[mid] > nums[q]:
                p = mid + 1
            else:
                q = mid - 1
        
        return -1
# @lc code=end

