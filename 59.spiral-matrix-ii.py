#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
from typing import *
# @lc code=start

def is_out_of_boundry(mat: List[List[int]], i: int, j: int) -> bool:
    if i >= len(mat) or j >= len(mat[0]) or i < 0 or j < 0:
        return True
    
    if mat[i][j] != 0:
        return True
    
    return False
    
STEPS: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]] = ((0, 1), (1, 0), (0, -1), (-1, 0))

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        steps_taken = 0
        step_index = 0
        i, j = 0, 0
        
        while True:
            if is_out_of_boundry(matrix, i, j):
                step_i, step_j = STEPS[step_index]
                i -= step_i
                j -= step_j
                step_index = (step_index + 1) % len(STEPS)
                if steps_taken == 0:
                    break
                steps_taken = 0
                step_i, step_j = STEPS[step_index]
                i += step_i
                j += step_j
                continue
        
            matrix[i][j] = num
            num += 1
            step_i, step_j = STEPS[step_index]
            i += step_i
            j += step_j
            steps_taken += 1
        
        return matrix
        
        
        
        
        
        
        
        
# @lc code=end

