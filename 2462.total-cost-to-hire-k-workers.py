#
# @lc app=leetcode id=2462 lang=python3
#
# [2462] Total Cost to Hire K Workers
#
from typing import *
import heapq
# @lc code=start
INT_MAX = 10e5 + 1
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        head_workers = []
        tail_workers = []
        
        for i in range(candidates):
            heapq.heappush(head_workers, (costs[i], i))
            heapq.heappush(tail_workers, (costs[len(costs) - 1 - i], len(costs) - 1 - i))
        
        chosen_workers = set()
        total_cost = 0
        head_end = candidates - 1
        tail_end = len(costs) - candidates
        for i in range(k):
            head_cost, head_index = heapq.nsmallest(1, head_workers)[0]
            while head_index in chosen_workers and len(head_workers):
                heapq.heappop(head_workers)
            head_cost, head_index = heapq.nsmallest(1, head_workers)[0]
                
            tail_cost, tail_index = heapq.nsmallest(1, tail_workers)[0]
            while tail_index in chosen_workers and len(tail_workers):
                heapq.heappop(tail_workers)
            tail_cost, tail_index = heapq.nsmallest(1, tail_workers)[0]
        
            chosen_index = 0
            
            head_removed = True
            if head_cost < tail_cost:
                chosen_index = head_index
            elif head_cost > tail_cost:
                chosen_index = tail_index  
                head_removed = False
            elif head_index < tail_index:
                chosen_index = head_index
            else:
                chosen_index = tail_index
                head_removed = False
            
            chosen_workers.add(chosen_index)
            total_cost += costs[chosen_index]
            if head_removed:
                heapq.heappop(head_workers)
                head_end += 1
                while head_end < len(costs) and head_end in chosen_workers:
                    head_end += 1
                if head_end < len(costs):
                    heapq.heappush(head_workers, (costs[head_end], head_end))
            else:
                heapq.heappop(tail_workers)
                tail_end -= 1
                while tail_end >= 0 and tail_end in chosen_workers:
                    tail_end -= 1
                if tail_end >=0 :
                    heapq.heappush(tail_workers, (costs[tail_end], tail_end))
            
        return total_cost
# @lc code=end

