from typing import *
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        smallest = nums[0]
        largest = nums[-1]
        
        min_small_index = 0
        max_large_index = len(nums) - 1
        
        for i in range(len(nums)):
          if nums[i] < smallest:
            min_small_index = i
            smallest = nums[i]
          if nums[len(nums) - 1 - i] > largest:
            max_large_index = len(nums) - 1 - i
            largest = nums[len(nums) - 1 - i]
        
        ans = min_small_index - 0 + len(nums) - 1 - max_large_index
        
        if min_small_index > max_large_index:
          ans -= 1
        
        return ans
        