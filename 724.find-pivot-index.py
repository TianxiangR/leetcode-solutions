#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
from typing import *
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0]
        suffixSum = [0]
        
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
        
        for num in reversed(nums):
            suffixSum.append(suffixSum[-1] + num)
        suffixSum.reverse()
        
        for i in range(len(nums)):
            if prefixSum[i] == suffixSum[i + 1]:
                return i
        
        return -1
        
# @lc code=end

