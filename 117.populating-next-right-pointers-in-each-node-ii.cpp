/*
 * @lc app=leetcode id=117 lang=cpp
 *
 * [117] Populating Next Right Pointers in Each Node II
 */
#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int val;
    Node *left;
    Node *right;
    Node *next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node *_left, Node *_right, Node *_next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
// @lc code=start
template <typename T>
inline T &queue_pop(queue<T> &q)
{
    T &rval = q.front();
    q.pop();
    return rval;
}

class Solution
{
public:
    Node *connect(Node *root)
    {

        if (root == NULL)
        {
            return NULL;
        }

        queue<Node *> curr_queue, next_queue;
        vector<Node *> level;
        vector<vector<Node *>> levels;

        curr_queue.push(root);
        level.push_back(root);
        levels.push_back(level);
        level = {};

        while (!curr_queue.empty())
        {
            Node *front = queue_pop(curr_queue);
            if (front->left != NULL)
            {
                level.push_back(front->left);
                next_queue.push(front->left);
            }
            if (front->right != NULL)
            {
                level.push_back(front->right);
                next_queue.push(front->right);
            }

            if (curr_queue.empty())
            {
                levels.push_back(level);
                level = {};
                swap(curr_queue, next_queue);
            }
        }

        for (auto &l : levels)
        {
            for (int i = 0; i + 1 < size(l); ++i)
            {
                l[i]->next = l[i + 1];
            }
        }

        return root;
    }
};
// @lc code=end
