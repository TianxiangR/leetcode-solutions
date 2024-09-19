#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#
from typing import *
# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[float('inf') for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        dp[-1][-1] = max(-1 * dungeon[-1][-1] + 1, 1)
        
        for i in reversed(range(len(dungeon))):
            for j in reversed(range(len(dungeon[0]))):
                if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
                    continue
                
                bottom = float('inf')
                right = float('inf')
                
                if i + 1 < len(dungeon):
                    bottom = dp[i + 1][j]
                
                if j + 1 < len(dungeon[0]):
                    right = dp[i][j + 1]
                
                dp[i][j] = max(min(dp[i][j], bottom, right) - dungeon[i][j], 1)

        return max(dp[0][0], 1)
# @lc code=end

