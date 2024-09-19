#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#
from typing import *
# @lc code=start
class TrieNode:
    def __init__(self, val: str):
        self.val: str = val
        self.branches: List[str | None] = [None for _ in range(26)]
        self.word = None

class Trie:

    def __init__(self):
        self.root = TrieNode("")
        self.length = 0
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            next = curr.branches[ord(c) - ord('a')]
            if next is None:
                next = TrieNode(c)
                curr.branches[ord(c) - ord('a')] = next
            curr = next
        
        curr.word = word
        self.length += 1
                         

    def search(self, word: str) -> bool:
        curr = self.root
        
        if self.length == 0:
            return False
        
        for c in word:
            next = curr.branches[ord(c) - ord('a')]
            if next is None:
                return False
            curr = next
            
        return curr.word is not None
    
class Solution:
    def _firstKWords(self, root: TrieNode, k: int) -> List[str]:
        output = []
        
        if root.word is not None:
            output.append(root.word)
        
        for i in range(26):
            branch = i
            if root.branches[branch] is not None:
                output.extend(self._firstKWords(root.branches[branch], k))
            if len(output) >= k:
                break
        
        return output[:k]
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        output = []
        trie = Trie()
        
        for product in products:
            trie.insert(product)
        
        curr = trie.root        
        
        for c in searchWord:
            if curr.branches[ord(c) - ord('a')] is not None:
                curr = curr.branches[ord(c) - ord('a')]
            else:
                curr = TrieNode("")
            output.append(self._firstKWords(curr, 3))
        
        return output
        
# @lc code=end

