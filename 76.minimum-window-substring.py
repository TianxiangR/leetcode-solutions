#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
import math
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charCount = len(t)
        charFreq = {}
        n = len(s)
        
        for c in t:
            charFreq[c] = charFreq.get(c, 0) + 1
        
        seen = {}
        charLeft = charCount
        left = 0
        window = ""
        windowLength = float('inf')
        
        
        for right in range(n):
            currentChar = s[right]
            if currentChar in charFreq:
                if currentChar == 'd':
                    pass
                seen[currentChar] = seen.get(currentChar, 0) + 1
                charLeft -= 1 if seen[currentChar] <= charFreq[currentChar] else 0
                
            if charLeft == 0:
                currentWindow = s[left: right + 1]
                if len(currentWindow) < windowLength:
                    window = currentWindow
                    windowLength = len(currentWindow)
                
                while True:
                    firstChar = s[left]
                    currentWindow = s[left: right + 1]
                    if len(currentWindow) < windowLength:
                        window = currentWindow
                        windowLength = len(currentWindow)
                    left += 1
                    if firstChar in seen:
                        seen[firstChar] -= 1
                        if seen[firstChar] < charFreq[firstChar]:
                            charLeft += 1
                            break
                    
        return window
                

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))

