#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
from typing import *
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search row
        p, q = 0, len(matrix) - 1
        
        target_row = None
        while p <= q:
            pivot = (p + q) // 2
            mid_row = matrix[pivot]
            
            if mid_row[0] > target:
                q = pivot - 1
            elif mid_row[-1] < target:
                p = pivot + 1
            else:
                target_row = mid_row
                break
        
        if target_row is None:
            return False

        p, q = 0, len(matrix[0]) - 1
        
        while p <= q:
            pivot = (p + q) // 2
            mid = target_row[pivot]
            
            if mid > target:
                q = pivot - 1
            elif mid < target:
                p = pivot + 1
            else:
                return True
        
        return False

            
        
# @lc code=end

