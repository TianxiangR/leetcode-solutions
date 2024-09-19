#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#
from typing import *
# @lc code=start
class Solution:      
    def longestSubarray(self, nums: List[int]) -> int:
        removed = nums[0] == 0
        ones = int(not removed)
        max_ones = 0
        start = 0
        for i in range(1, len(nums)):
            if nums[i] == 1:
                ones += 1
            
            elif removed:
                while True:
                    if nums[start] == 0:
                        start += 1
                        break
                    start += 1
                    ones -= 1
            else:
                removed = True
            
            max_ones = max(ones - int(not removed), max_ones)
        
        return max_ones
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.longestSubarray([1,1,0,0,1,1,1,0,1])

