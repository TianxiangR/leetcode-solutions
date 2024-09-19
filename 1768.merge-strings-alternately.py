#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#
from typing import *
# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        words = [word1, word2]
        indices = [0, 0]
        turn = 0
        output = ""
        while indices[0] < len(word1) or indices[1] < len(word2):
            word = words[turn]
            index = indices[turn]
            
            output += word[index]
            indices[turn] += 1
            turn = (turn + 1) % 2
            
            if indices[turn] == len(words[turn]):
                turn = (turn + 1) % 2
        
        return output
# @lc code=end

