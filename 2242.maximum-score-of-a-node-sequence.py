#
# @lc app=leetcode id=2242 lang=python3
#
# [2242] Maximum Score of a Node Sequence
#
from typing import *
import heapq
# @lc code=start
class Solution:
    def _kLargest(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(num) > k:
                heapq.heappop(heap)
        
        return heap
    
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        
        
# @lc code=end

