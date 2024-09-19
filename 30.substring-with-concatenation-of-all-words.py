#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
from typing import *
# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        wordCount = len(words)
        n = len(s)
        wordFreq = {}
        answer = []
        
        for word in words:
            wordFreq[word] = wordFreq.get(word, 0) + 1
        
        for i in range(wordLen):
            left = i
            wordsLeft = wordCount
            seen = {}
            right = i + wordLen

            for right in range(i, n - wordLen, wordLen):
                if right + wordLen - left > wordLen * wordCount:
                    firstWord = s[left: left + wordLen]
                    left += wordLen
                    if firstWord in seen:
                        seen[firstWord] -= 1
                        wordsLeft += 1
                if left == 82:
                    pass

                currentWord = s[right: right + wordLen]
                if currentWord == 'aab':
                    print(left)
                if currentWord in wordFreq:
                    seen[currentWord] = seen.get(currentWord, 0) + 1
                    wordsLeft -= 1
                    if seen[currentWord] > wordFreq[currentWord]:
                        while seen[currentWord] > wordFreq[currentWord]:
                            firstWord = s[left: left + wordLen]
                            left += wordLen
                            if firstWord in seen:
                                seen[firstWord] -= 1
                                wordsLeft += 1
                else:
                    # reset
                    seen = {}
                    wordsLeft = wordCount
                    left = right + wordLen

                if wordsLeft == 0:
                    answer.append(left)
        
        return answer
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring("abbaccaaabcabbbccbabbccabbacabcacbbaabbbbbaaabaccaacbccabcbababbbabccabacbbcabbaacaccccbaabcabaabaaaabcaabcacabaa", ["cac","aaa","aba","aab","abc"]))

