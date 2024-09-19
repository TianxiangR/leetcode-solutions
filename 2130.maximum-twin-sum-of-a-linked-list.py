#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
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
        
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        curr = head
        
        while curr is not None:
            length += 1
            curr = curr.next
        
        mid = length // 2
        first_half_head = head
        first_half_tail = head
        for i in range(mid - 1):
            first_half_tail = first_half_tail.next
        
        second_half_head = first_half_tail.next
        second_half_head = self.reverseList(second_half_head)
        
        curr1 = first_half_head
        curr2 = second_half_head
        
        max_sum = 0
        for i in range(mid):
            _sum = curr1.val + curr2.val
            max_sum = max(max_sum, _sum)
            curr1 = curr1.next
            curr2 = curr2.next
        
        return max_sum

# @lc code=end

