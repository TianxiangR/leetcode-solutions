#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
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
import math
class Solution:
    def _mergeSort(self, head: Optional[ListNode], tail: Optional[ListNode]) -> tuple[Optional[ListNode], Optional[ListNode]]:
        if head == tail:
            return [head, tail]
        
        # get the length of the linked list
        length = 0
        curr = head
        
        while curr != tail.next:
            length += 1
            curr = curr.next
        
        if length == 2:
            if tail.val < head.val:   
                head.next = tail.next
                tail.next = head
                temp = tail
                tail = head
                head = temp
            return [head, tail]

        pivot = math.ceil(length / 2)
        first_half_head: ListNode = head
        first_half_tail: ListNode = head
        for i in range(pivot - 1):
            first_half_tail = first_half_tail.next
        
        second_half_head: ListNode = first_half_tail.next
        second_half_tail: ListNode = second_half_head
        for i in range(pivot, length - 1):
            second_half_tail = second_half_tail.next
        
        first_half_tail.next = None
        if second_half_tail is not None:
            second_half_tail.next = None
        
        first_half_result = self._mergeSort(first_half_head, first_half_tail)
        second_half_result = self._mergeSort(second_half_head, second_half_tail)
        
        if first_half_result[0] is None:
            return second_half_result

        if second_half_result[0] is None:
            return second_half_result
         
        rhead = None
        rtail = None
        
        fhead = first_half_result[0]
        ftail = first_half_result[1]
        shead = second_half_result[0]
        stail = second_half_result[1]
        
        while fhead is not None or shead is not None:
            curr: Optional[ListNode] = None
            if fhead is not None:
                curr = curr if curr is not None and curr.val < fhead.val else fhead
            if shead is not None:
                curr = curr if curr is not None and curr.val < shead.val else shead
            
            if curr == fhead:
                fhead = fhead.next
            
            if curr == shead:
                shead = shead.next
            
            if rhead is None:
                rhead = curr
                rtail = curr
            else:
                rtail.next = curr
                rtail = curr
        
        return [rhead, rtail]
                

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #  get tail
        tail = head
        while tail is not None and tail.next is not None:
            tail = tail.next
        
        return self._mergeSort(head, tail)[0]
        
        
# @lc code=end

