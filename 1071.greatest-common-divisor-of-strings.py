#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#
from typing import *
# @lc code=start
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        concat1 =  str1 + str2
        concat2 = str2 + str1
        
        if concat1 != concat2:
            return ""
        
        gcd_len = math.gcd(len(str1), len(str2))
        return str1[:gcd_len]    
            
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    
    str1 = "ABCABC"
    str2 = "ABC"
    
    print(solution.gcdOfStrings(str1, str2))
