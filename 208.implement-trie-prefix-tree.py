#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
from typing import *
# @lc code=start
class TrieNode:
    def __init__(self, val: str):
        self.val: str = val
        self.branches: dict[str, 'TrieNode'] = dict()
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode("")
        self.length = 0
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            next = curr.branches.get(c)
            if next is None:
                next = TrieNode(c)
                curr.branches[c] = next
            curr = next
        
        curr.is_word = True
        self.length += 1
                         

    def search(self, word: str) -> bool:
        curr = self.root
        
        if self.length == 0:
            return False
        
        for c in word:
            next = curr.branches.get(c)
            if next is None:
                return False
            curr = next
            
        return curr.is_word


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        if self.length == 0:
            return False
        
        for c in prefix:
            next = curr.branches.get(c)
            if next is None:
                return False
            curr = next
        
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

if __name__ == "__main__":
    trie = Trie()
    trie.insert("hotdog")
    trie.startsWith("dog")
