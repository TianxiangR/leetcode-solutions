#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
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
# @lc code=end

