#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#
from typing import *
# @lc code=start
class Solution:
    MODULO_FACTOR = int(10e9 - 7)
    def numTilings(self, n: int) -> int:
        f = [1, 2]
        p = [0, 1]
        
        for i in range(2, n):
            f.append((f[i - 1] + f[i - 2] + p[i - 1] * 2) % Solution.MODULO_FACTOR)
            p.append((f[i - 2] + p[i - 1]) % Solution.MODULO_FACTOR)
        
        return f[n - 1]
        
        
# @lc code=end

