#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        count = 0
        curr = head
        prev = None
        start = None
        end = None
        saved_next = None
        r_head = None
        while curr is not None:
            count += 1
            if count % k == 1:
                start = curr
            if count % k == 0:
                saved_prev = prev
                end = curr
                saved_next = curr.next
                curr = start
                for i in range(k):
                    next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next
                if saved_prev is not None:
                    saved_prev.next = end

                start.next = saved_next
                curr = start
                prev = curr
                
                if r_head is None:
                    r_head = end
            
            curr = curr.next
        
        return r_head
                

# @lc code=end

