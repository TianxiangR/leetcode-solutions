#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = 0
        
        if head is None:
            return head
        
        while curr is not None:
            length += 1
            curr = curr.next
        
        mid = length // 2
        curr: 'ListNode' = None
        prev: 'ListNode' = None
        for i in range(mid):
            if curr is None:
                curr = head
            else:
                curr = curr.next
                prev = curr
        
        if prev is not None:
            prev.next = curr.next
            curr.next = None
        else:
            head = curr.next
            curr.next = None
        
        return head
        
# @lc code=end

