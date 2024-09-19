/*
 * @lc app=leetcode id=124 lang=cpp
 *
 * [124] Binary Tree Maximum Path Sum
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
private:
    vector<int> helper(TreeNode *root)
    {
        if (root == NULL)
        {
            return {0, 0};
        }

        if (root->left == NULL && root->right == NULL)
        {
            return {root->val, root->val};
        }

        vector<int> left = {INT_MIN, INT_MIN}, right = {INT_MIN, INT_MIN};

        if (root->left != NULL)
        {
            left = helper(root->left);
        }

        if (root->right != NULL)
        {
            right = helper(root->right);
        }

        int max_inclusive = root->val, max_exclusive = 0;

        max_inclusive = max(max(
            (long long) max_inclusive,
            max_inclusive + (long long)left[0]
            ),
            max_inclusive + (long long)right[0]
        );

        max_exclusive = max(
            (long long)max_inclusive,
            max((long long)left[1], (long long)right[1]));
        
        max_exclusive = max((long long) max_exclusive, (long long) root->val + left[0] + right[0]);

        return {max_inclusive, max_exclusive};
    }

public:
    int maxPathSum(TreeNode *root)
    {
        vector<int> rval = helper(root);
        return max(rval[0], rval[1]);
    }
};
// @lc code=end
