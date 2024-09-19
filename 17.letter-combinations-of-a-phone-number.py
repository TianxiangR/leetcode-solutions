#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import *
# @lc code=start
key_mapping = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        combinations = [""]
        
        for digit in reversed(digits):
            new_comb = []
            letters = key_mapping[digit]
            for c in letters:
                for comb in combinations:
                    new_comb.append(c + comb)
            
            combinations = new_comb
        
        
        return combinations
            
        
# @lc code=end

