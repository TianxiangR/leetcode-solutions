#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#
import heapq
# @lc code=start
class SmallestInfiniteSet:

    def __init__(self):
        self.removed_nums = set()
        self.curr_integer = 1
        self.heap = []

    def popSmallest(self) -> int:
        if len(self.heap) > 0:
            popped = heapq.heappop(self.heap)
            self.removed_nums.add(popped)
            return popped
        else:
            self.removed_nums.add(self.curr_integer)
            self.curr_integer += 1
            return self.curr_integer - 1
                        
                

    def addBack(self, num: int) -> None:
        if num in self.removed_nums:
            self.removed_nums.remove(num)
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

