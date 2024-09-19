from typing import *
from collections import deque
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        p, q = 0, len(nums) - 1
        
        count = 0
        while p < q:
          front, back = nums[p], nums[q]
          
          if front < back:
            nums[p + 1] += nums[p]
            count += 1
            q += 1
          elif front > back:
            nums[q - 1] += nums[q]
            count += 1
            p -= 1
          
          p += 1
          q -= 1

        return count
        

        
              