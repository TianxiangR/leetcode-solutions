#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = None
        p1 = list1
        p2 = list2
        
        if p1 is None:
            return p2
        
        if p2 is None:
            return p1
        
        if p1.val < p2.val:
            head = p1
            curr = head
            p1 = p1.next
        else:
            head = p2
            curr = head
            p2 = p2.next
        
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                curr.next = p1
                curr = p1
                p1 = p1.next
            else:
                curr.next = p2
                curr = p2
                p2 = p2.next
            
        while p1 is not None:
            curr.next = p1
            curr = p1
            p1 = p1.next
        
        while p2 is not None:
            curr.next = p2
            curr = p2
            p2 = p2.next
        
        return head
                
# @lc code=end

