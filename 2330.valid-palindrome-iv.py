class Solution:
    def makePalindrome(self, s: str) -> bool:
        p, q = 0, len(s) - 1
        operations_left = 2
        
        while p < q:
          if s[p] != s[q]:
            operations_left -= 1
          p += 1
          q -= 1
          
          if operations_left < 0:
            return False
        
        return operations_left >= 0