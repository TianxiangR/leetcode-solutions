/*
 * @lc app=leetcode id=82 lang=cpp
 *
 * [82] Remove Duplicates from Sorted List II
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
    ListNode *deleteDuplicates(ListNode *head)
    {
        if (head == NULL)
            return NULL;

        ListNode *answer = head, *curr = head, *prev = NULL;

        while (curr != NULL && curr->next != NULL)
        {
            if (curr->val == curr->next->val)
            {
                int val = curr->val;
                while (curr != NULL && curr->val == val)
                {
                    curr = curr->next;
                }

                if (prev == NULL)
                {
                    answer = curr;
                }
                else
                {
                    prev->next = curr;
                }
            }
            else
            {
                prev = curr;
                curr = curr->next;
            }
        }

        return answer;
    }
};
// @lc code=end
