#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#
import math
# @lc code=start
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # naive approach
        divisors = []
        sqrt_n = math.sqrt(n)
        
        for i in range(1, int(sqrt_n + 1)):
            if n % i == 0:
                divisors.append(i)
                k -= 1
            if k == 0:
                return i
        
        if sqrt_n ** 2 == n:
            k += 1
        
        return n // divisors[len(divisors) - k] if k <= len(divisors) else -1
            
            
        
# @lc code=end

