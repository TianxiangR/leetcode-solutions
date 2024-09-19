/*
 * @lc app=leetcode id=92 lang=cpp
 *
 * [92] Reverse Linked List II
 */
#include <bits/stdc++.h>
using namespace std;
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *reverseBetween(ListNode *head, int left, int right)
    {
        int index = 1;
        ListNode *curr = head, *prev = NULL, *next = NULL, *mid_next = NULL, *mid_tail, *answer, *mid_head;

        while (index < left)
        {
            prev = curr;
            curr = curr->next;
            index++;
        }

        mid_tail = curr;
        mid_head = curr;
        mid_next = curr;
        curr = curr->next;
        index++;
        while (index <= right)
        {
            next = curr->next;
            curr->next = mid_next;
            mid_next = curr;
            mid_head = curr;
            curr = next;
            index++;
        }

        if (prev != NULL)
        {
            answer = head;
            prev->next = mid_head;
        }
        else
        {
            answer = mid_head;
        }

        mid_tail->next = curr;

        return answer;
    }
};
// @lc code=end
