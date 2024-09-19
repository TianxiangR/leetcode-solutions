#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#
from typing import *
import heapq
# @lc code=start
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        indices = [i for i in range(len(nums1))]
        indices.sort(key=lambda i: nums2[i], reverse=True)
        nums1_sorted = []
        nums2_sorted = []
        
        for index in indices:
            nums1_sorted.append(nums1[index])
            nums2_sorted.append(nums2[index])
        
        
        heap = []
        _sum = 0
        for i in range(k):
            heapq.heappush(heap, nums1_sorted[i])
            _sum += nums1_sorted[i]
        
        max_score = sum(heap) * nums2_sorted[k - 1]
        for i in range(k, len(nums1)):
            heapq.heappush(heap, nums1_sorted[i])
            _sum += nums1_sorted[i]
            _sum -= heapq.heappop(heap)
            
            score = _sum * nums2_sorted[i]
            max_score = max(max_score, score)
        
        return max_score
                    
# @lc code=end

