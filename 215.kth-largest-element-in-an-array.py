#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
from typing import *
import heapq
# @lc code=start
class Solution:
    INT_MIN = int(-10e4 - 1)
    INT_MAX = int(10e4 + 1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappush(heap, num)
                heapq.heappop(heap)
                
        

        return heapq.heappop(heap)
        
# @lc code=end

