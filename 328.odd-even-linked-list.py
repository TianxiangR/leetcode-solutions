#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = 0
        curr = head
        even_head = None
        even_curr = None
        even_prev = None
        odd_head = None
        odd_curr = None
        odd_prev = None
        while curr is not None:
            if index % 2 == 1:
                if even_head is None:
                    even_head = curr
                    even_curr = curr
                else:
                    even_curr.next = curr
                    even_curr = curr
            else:
                if odd_head is None:
                    odd_head = curr
                    odd_curr = curr
                else:
                    odd_curr.next = curr
                    odd_curr = curr
            index += 1
            curr = curr.next
        
        if odd_curr is None:
            return even_head
        
        odd_curr.next = even_head
        if even_curr is not None:
            even_curr.next = None
        
        return odd_head
        
# @lc code=end

