/*
 * @lc app=leetcode id=129 lang=cpp
 *
 * [129] Sum Root to Leaf Numbers
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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution
{
public:
    int sumNumbers(TreeNode *root, int prev = 0)
    {
        if (root == NULL)
        {
            return prev;
        }

        prev = 10 * prev + root->val;
        int left = 0, right = 0;

        if (root->left != NULL)
        {
            left = sumNumbers(root->left, prev);
        }

        if (root->right != NULL)
        {
            right = sumNumbers(root->right, prev);
        }

        if (left == 0 && right == 0)
        {
            return prev;
        }

        return left + right;
    }
};
// @lc code=end
