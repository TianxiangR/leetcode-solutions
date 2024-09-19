#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

from typing import *
# @lc code=start
class TrieNode:
    def __init__(self, val: str, branches: dict[str, 'TrieNode'] = None, is_word: bool = False):
        self.val: str = val
        self.branches: dict[str, 'TrieNode'] = {} if branches is None else branches
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            next = curr.branches.get(c)
            if next is None:
                next = TrieNode(c)
                curr.branches[c] = next
            
            curr = next
        
        curr.is_word = True
        
    
    def searchFrom(self, root: TrieNode, word: str) -> bool:
        curr = root
        
        for i in range(len(word)):
            c = word[i]
            if c == ".":
                for branchNode in curr.branches.values():
                      if self.searchFrom(branchNode, word[i + 1:]):
                          return True
                return False
            
            next = curr.branches.get(c)
            if next is None:
                return False
            
            curr = next
        
        return curr.is_word
        
                    
    def search(self, word: str) -> bool:
        return self.searchFrom(self.root, word)
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

if __name__ == "__main__":
    wordDict = WordDictionary()
    
    wordDict.addWord("bad")
    wordDict.search("b..")
