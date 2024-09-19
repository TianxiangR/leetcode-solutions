/*
 * @lc app=leetcode id=86 lang=cpp
 *
 * [86] Partition List
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
    ListNode *partition(ListNode *head, int x)
    {
        ListNode *answer = NULL, *prev = NULL, *start = NULL, *end = NULL, *curr = head;

        while (curr != NULL)
        {
            if (curr->val < x)
            {
                if (prev == NULL)
                {
                    prev = curr;
                    answer = curr;
                }
                else
                {
                    prev->next = curr;
                    prev = curr;
                }
            }
            else
            {
                if (start == NULL)
                {
                    start = curr;
                    end = curr;
                }
                else
                {
                    end->next = curr;
                    end = curr;
                }
            }
            curr = curr->next;
        }

        if (prev == NULL)
        {
            answer = start;
        }
        else
        {
            prev->next = start;
        }

        if (end != NULL)
        {
            end->next = NULL;
        }

        return answer;
    }
};
// @lc code=end
