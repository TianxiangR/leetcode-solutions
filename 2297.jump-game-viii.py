from typing import *

class Solution:
    def _getNextGreaterOrEqual(self, nums: List[int]) -> List[int]:
        stack = []
        nge = [-1 for _ in nums]
        
        for i in reversed(range(len(nums))):
          while len(stack) and nums[stack[-1]] < nums[i]:
            stack.pop()
          
          if len(stack):
            nge[i] = stack[-1]
          
          stack.append(i)
        
        return nge
    
    def _getNextSmaller(self, nums: List[int]) -> List[int]:
        stack = []
        ns = [-1 for _ in nums]
        
        for i in reversed(range(len(nums))):
          while len(stack) and nums[stack[-1]] >= nums[i]:
            stack.pop()
          
          if len(stack):
            ns[i] = stack[-1]
          
          stack.append(i)
        
        return ns
  
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        nge  = self._getNextGreaterOrEqual(nums)
        ns = self._getNextSmaller(nums)
        dp = [float('inf') for _ in nums]
        dp[0] = 0
        
        for i in range(len(nums) - 1):
          # take nge
          next_greater = nge[i]
          if next_greater > -1:
            dp[next_greater] = min(dp[next_greater], dp[i] + costs[next_greater])
          
          # take ns
          next_smaller = ns[i]
          if next_smaller > -1:
            dp[next_smaller] = min(dp[next_smaller], dp[i] + costs[next_smaller])
        
        return dp[-1]
        
        