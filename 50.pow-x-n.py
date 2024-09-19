#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
             return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x * x, (n - 1) // 2)
        
# @lc code=end

