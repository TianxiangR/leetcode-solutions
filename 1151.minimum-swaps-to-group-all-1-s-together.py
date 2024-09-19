from typing import *
from collections import Counter
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        total_ones = Counter(data)[1]

        curr_ones = Counter(data[:total_ones])[1]
        min_swaps = total_ones - curr_ones
        
        for i in range(total_ones, len(data)):
          if data[i] == 1:
            curr_ones += 1

          if data[i - total_ones] == 1:
            curr_ones -= 1
            
          min_swaps = min(min_swaps, total_ones - curr_ones)
        
        return min_swaps
          