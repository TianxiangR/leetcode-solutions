#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
from typing import *
# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        p = 0
        count = 0
        i = 0
        j = 0
        
        while i < len(chars):
            c = chars[i]
            count = 1
            j = i + 1
            while j < len(chars) and chars[j] == c:
                j += 1
                count += 1
            i = j
            chars[p] = c
            p += 1
            if count > 1:
                count_str = str(count)
                for k in range(len(count_str)):
                    chars[p] = count_str[k]
                    p += 1
                
        # while len(chars) > p:
        #     chars.pop()
        
        return p
        
# @lc code=end

