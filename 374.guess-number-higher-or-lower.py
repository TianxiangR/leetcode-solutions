#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

def guess(num: int) -> int:
    return 0
# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        p = 1
        q = n
        while p <= q:
            mid = (p + q) // 2
            result = guess(mid)
            if result == 0:
                return mid
            if result == -1:
                q = mid - 1
            else:
                p = mid + 1
        
        return 0
        
# @lc code=end

