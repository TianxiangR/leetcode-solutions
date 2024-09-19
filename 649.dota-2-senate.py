#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#
from typing import *
# @lc code=start
class ListNode:
    def __init__(self, val: str, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad_count = 0
        dire_count = 0
        head = None
        curr = None
        for i in range(len(senate)):
            if senate[i] == "R":
                rad_count += 1
            else:
                dire_count += 1
            if head is None:
                head = ListNode(senate[i])
                curr = head
            else:
                curr.next = ListNode(senate[i])
                curr = curr.next
        
        ban_r = 0
        ban_d = 0
        while rad_count > 0 and dire_count > 0:
            curr: ListNode = head
            prev: ListNode = None
            while curr is not None:
                remove = False
                if curr.val == "R":
                    if ban_r > 0:
                        ban_r -= 1
                        rad_count -= 1
                        remove = True

                    else:
                        ban_d += 1
                else:
                    if ban_d > 0:
                        ban_d -= 1
                        dire_count -= 1
                        remove = True
                    else:
                        ban_r += 1
                
                if remove:
                    # remove node
                    if curr == head:
                        head = curr.next
                    
                    if prev is not None:
                        prev.next = curr.next
                else:
                    prev = curr
                
                curr = curr.next
        
        return "Radiant" if rad_count > 0 else "Dire"
                        

        
        
        
# @lc code=end

