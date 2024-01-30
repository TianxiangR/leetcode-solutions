/*
 * @lc app=leetcode id=238 lang=cpp
 *
 * [238] Product of Array Except Self
 */

// @lc code=start
class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        int len = nums.size();
        vector<int> ans(len);

        int left = 1, right = 1;
        ans[0] = left;
        for (int i = 1; i < len; ++i)
        {
            left *= nums[i - 1];
            ans[i] = left;
        }

        for (int i = len - 2; i >= 0; --i)
        {
            right *= nums[i + 1];
            ans[i] *= right;
        }

        return ans;
    }
};
// @lc code=end
