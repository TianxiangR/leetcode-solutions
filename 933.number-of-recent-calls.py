#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
from collections import deque
class RecentCounter:

    def __init__(self):
        self.deque: deque[int] = deque()

    def ping(self, t: int) -> int:
        while len(self.deque) > 0 and t - self.deque[0] > 3000:
            self.deque.popleft()
        
        self.deque.append(t)
        return len(self.deque)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

