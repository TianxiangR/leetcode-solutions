#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        # init
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
                
        max_vowels = vowel_count
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                vowel_count -= 1
            if s[i] in vowels:
                vowel_count += 1
            
            max_vowels = max(max_vowels, vowel_count)
        
        return max_vowels
        
# @lc code=end

