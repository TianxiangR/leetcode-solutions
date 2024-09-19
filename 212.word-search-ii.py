#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
from typing import *
# @lc code=start
class TrieNode:
    def __init__(self, val: str, branches: Optional[dict[str, 'TrieNode']] = None, word: Optional[str] = None):
        self.val: str = val
        self.branches: dict[str, 'TrieNode'] = {} if branches is None else branches
        self.word: Optional[str] = word

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
        
        curr.word = word
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
            
        return curr.word is not None

class Solution:
    def _is_valid_position(self, board: List[List[str]], i: int, j: int) -> bool:
        return 0 <= i < len(board) and 0 <= j < len(board[0])
    
    def _get_neighbors(self, board: List[List[str]], i: int, j: int) -> list[tuple[int]]:
        output = []
        
        if i > 0:
            output.append((i - 1, j))
        if j > 0:
            output.append((i, j - 1))
        if i < len(board) - 1:
            output.append((i + 1, j))
        if j < len(board[0]) - 1:
            output.append((i, j + 1))
        
        return output
    
    def searchFrom(self, board: List[List[str]], i: int, j: int, curr_node: TrieNode) -> set[str]:        
        c = board[i][j]
        output = set()
        if c in curr_node.branches:
            next = curr_node.branches[c]
            if next.word is not None:
                output.add(next.word)
                if len(next.branches) == 0:
                    return output
                
            neighbors = self._get_neighbors(board, i, j)
            saved_char = c
            board[i][j] = "#"
            
            for neighbor in neighbors:
                search_result = self.searchFrom(board, neighbor[0], neighbor[1], next)
                output = output.union(search_result)
            board[i][j] = saved_char
        return output
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()
        
        for word in words:
            self.trie.insert(word)
        
        output = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                search_result = self.searchFrom(board, i, j, self.trie.root)
                if search_result is not None:
                    output = output.union(search_result)
        
        return list(output)
                        
                    
        
        
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
    words = ["oa","oaa"]

    solution.findWords(board, words)
