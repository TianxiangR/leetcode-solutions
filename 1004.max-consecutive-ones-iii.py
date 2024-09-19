#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
from typing import *
# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        remaining = k
        max_ones = 0
        ones = 0
        
        for i in range(k):
            if nums[i] == 0:
                remaining -= 1
            ones += 1
        
        start = 0
        end = k - 1
        max_ones = ones
        
        while end < len(nums):
            if end + 1 < len(nums):
                if nums[end + 1] == 0 and remaining > 0:
                    ones += 1
                    remaining -= 1
                elif nums[end + 1] == 1:
                    ones += 1
                elif nums[end + 1] == 0 and remaining == 0:
                    while remaining == 0:
                        if nums[start] == 0:
                            remaining += 1
                        ones -= 1
                        start += 1
                    ones += 1
                    remaining -= 1     
            end += 1
            max_ones = max(max_ones, ones)
        return max_ones
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)