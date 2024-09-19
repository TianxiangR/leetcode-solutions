from typing import *

class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        dp = [books[0]]
        
        for i in range(1, len(books)):
          dp.append()