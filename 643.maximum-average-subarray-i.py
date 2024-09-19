#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
from typing import *
# @lc code=start
class Solution:    
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 0:
            return 0.0
        
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
        
        maxAverage = min(nums)
        for i in range(len(nums) - k + 1):
            average = (prefixSum[i + k] - prefixSum[i]) / k
            maxAverage = max(maxAverage, average)
            
        return maxAverage
                
# @lc code=end

