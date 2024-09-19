#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
from typing import *
# @lc code=start
INT_MAX = 2147483647
class Solution:
    def _solve(self, coins: List[int], amount: int) -> int:
        if amount in self.dp:
            return self.dp[amount]
        
        output = INT_MAX
        for c in coins:
            remaining = amount - c
            if remaining == 0:
                self.dp[amount] = min(self.dp.get(amount, INT_MAX), 1)
                return self.dp.get(amount)
            elif remaining > 0:
                sub_minimal = self._solve(coins, remaining)
                output = min(output, sub_minimal + 1)
        
        self.dp[amount] = output
        return output
                    
    
    def coinChange(self, coins: List[int], amount: int) -> int:        
        self.dp: dict[int, int] = {0: 0}
        
        output = self._solve(coins, amount)
        
        return output if output != INT_MAX else -1
        
# @lc code=end

