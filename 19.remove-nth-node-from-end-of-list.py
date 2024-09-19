#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        queue = []
        prev = None
        r_head = head
        curr = head
        
        while curr is not None:
            queue.append(curr)
            if len(queue) == n + 1:
                prev = queue.pop(0)
            curr = curr.next
            
        front = queue.pop(0)
        if prev is None:
            r_head = front.next
        else:
            prev.next = front.next
            front.next = None
        
        return r_head
            
                
            
            
# @lc code=end

