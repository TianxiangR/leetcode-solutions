#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from typing import *
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        p, q = 0, len(height) - 1
        
        max_area = 0
        while p < q:
            area = min(height[p], height[q]) * (q - p)
            max_area = max(max_area, area)
            
            if height[p] < height[q]:
                p += 1
            elif height[p] > height[q]:
                q -= 1
            elif height[p + 1] > height[q - 1]:
                p += 1
            elif height[p + 1] < height[q - 1]:
                q -= 1
            else:
                p += 1
        
        return max_area
            
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    a = solution.maxArea([1,3,2,5,25,24,5])
    print(a)

