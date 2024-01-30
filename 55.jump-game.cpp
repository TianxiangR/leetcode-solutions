/*
 * @lc app=leetcode id=55 lang=cpp
 *
 * [55] Jump Game
 */

// @lc code=start
class Solution
{
public:
    bool canJump(vector<int> &nums)
    {
        int max_length = 0;

        for (int i = 0; i < nums.size(); ++i)
        {
            if (max_length >= i)
            {
                max_length = max(max_length, i + nums[i]);
            }
            else
            {
                return false;
            }
        }

        return true;
    }
};
// @lc code=end
