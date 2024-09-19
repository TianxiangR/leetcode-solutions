/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
 */
#include <bits/stdc++.h>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
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
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *answer = NULL, *prev=NULL;
        int carry = 0;

        while(l1 != NULL || l2 != NULL || carry)
        {
            int sum = carry;
            if (l1 != NULL)
            {
                sum += l1->val;
                l1 = l1->next;
            }

            if (l2 != NULL)
            {
                sum += l2->val;
                l2 = l2->next;
            }

            if (sum >= 10)
            {
                carry = 1;
                sum -= 10;
            }
            else
            {
                carry = 0;
            }

            ListNode *curr = new ListNode(sum);

            if (answer == NULL)
            {
                answer = curr;
            }
            else
            {
                prev->next = curr;
            }
            prev = curr;
        }

        return answer;
    }
};
// @lc code=end

