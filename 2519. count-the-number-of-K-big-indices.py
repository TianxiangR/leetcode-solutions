from typing import *
import heapq
class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        # first pass, initialize the data structure
        prefix = [False for _ in nums]
        
        # second pass, check condition 1 for all numbers
        max_heap = []
        for i in range(len(nums)):
          num = nums[i]
          if len(max_heap) == k and -max_heap[0] < num:
            prefix[i] = True
          heapq.heappush(max_heap, -num)

          if len(max_heap) > k:
            heapq.heappop(max_heap)
        
        # third pass, check if condition 2 is satisfied and increment count if condition 1 is also satisfied
        max_heap = []
        count = 0
        for i in reversed(range(len(nums))):
          num = nums[i]
          if len(max_heap) == k and -max_heap[0] < num and prefix[i]:
            count += 1
          heapq.heappush(max_heap, -num)

          if len(max_heap) > k:
            heapq.heappop(max_heap)
        
        return count
        

        
        
        