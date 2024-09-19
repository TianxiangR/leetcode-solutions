#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        before_head = None
        before_tail = None
        after_head = None
        start = None
        end = None
        index = 1
        curr = head
        
        while curr is not None:
            if index < left:
                if before_head is None:
                    before_head = curr
                before_tail = curr
            elif left <= index <= right:
                if start is None:
                    start = curr
                    end = curr
                else:
                    end = curr
            else:
                if after_head is None:
                    after_head = curr

            curr = curr.next
            index += 1
        
        end.next = None
        new_start = self.reverseList(start)
        
        rhead = before_head
        
        if before_tail is not None:
            before_tail.next = new_start
        else:
            rhead = new_start
        
        start.next = after_head
        
        return rhead   
# @lc code=end

