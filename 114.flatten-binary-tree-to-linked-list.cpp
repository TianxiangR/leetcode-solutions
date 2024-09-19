/*
 * @lc app=leetcode id=114 lang=cpp
 *
 * [114] Flatten Binary Tree to Linked List
 */
#include <bits/stdc++.h>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// @lc code=start
template <typename T>
bool isLeaf(T *node)
{
    return node->left == NULL && node->right == NULL;
}

class Solution
{

private:
    pair<TreeNode *, TreeNode *> dfs(TreeNode *root)
    {
        if (root == NULL || isLeaf(root))
        {
            return {root, root};
        }

        TreeNode *curr_tail = root, *original_left = root->left, *original_right = root->right;
        root->left = NULL;
        root->right = NULL;

        if (original_left != NULL)
        {
            auto left_list = dfs(original_left);
            curr_tail->right = left_list.first;
            curr_tail = left_list.second;
        }

        if (original_right != NULL)
        {
            auto right_list = dfs(original_right);
            curr_tail->right = right_list.first;
            curr_tail = right_list.second;
        }

        return {root, curr_tail};
    }

public:
    void flatten(TreeNode *root)
    {
        dfs(root);
        return;
    }
};
// @lc code=end
