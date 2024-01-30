#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start

roman_table = {
    "I" : 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D" : 500,
    "M": 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII") \
         .replace("XL", "XXXX").replace("XC", "LXXXX") \
         .replace("CD", "CCCC").replace("CM", "DCCCC")
    
        for c in s:
            answer += roman_table[c]
            
        return answer
        
# @lc code=end


if __name__ == "__main__":
    Solution().romanToInt("MCMXCIV")

