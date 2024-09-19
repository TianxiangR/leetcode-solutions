/*
 * @lc app=leetcode id=138 lang=cpp
 *
 * [138] Copy List with Random Pointer
 */
#include <bits/stdc++.h>
using namespace std;
class Node
{
public:
    int val;
    Node *next;
    Node *random;

    Node(int _val)
    {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
// @lc code=start
// Definition for a Node.

class Solution
{
public:
    Node *copyRandomList(Node *head)
    {
        if (head == NULL)
        {
            return NULL;
        }

        unordered_map<Node *, Node *> map;
        Node *curr = head;
        Node *copy = new Node(curr->val), *copy_head = copy;

        map[curr] = copy;
        curr = curr->next;

        while (curr != NULL)
        {
            Node *new_node = new Node(curr->val);
            copy->next = new_node;
            copy = new_node;
            map[curr] = copy;
            curr = curr->next;
        }

        curr = head;
        copy = copy_head;
        while (curr != NULL)
        {
            copy->random = map[curr->random];
            curr = curr->next;
            copy = copy->next;
        }

        return copy_head;
    }
};
// @lc code=end

int main()
{
}
