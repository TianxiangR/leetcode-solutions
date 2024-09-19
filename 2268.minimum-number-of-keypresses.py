from collections import Counter
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = Counter(s)
        letters = list(counter.keys())
        
        # sort in descending order
        # because the more this letter is needed, the more key presses it needs
        # so we'd better to bind it early so that it requires lesser key presses
        letters.sort(key=lambda i: -counter[i])
        key_presses = 1
        key_bind = 1
        ans = 0
        
        for letter in letter:
          ans += key_presses * counter[letter]
          if key_bind == 9:
            key_presses += 1
            key_bind = 1
          else:
            key_bind += 1
        
        return ans
        