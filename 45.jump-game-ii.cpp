/*
 * @lc app=leetcode id=45 lang=cpp
 *
 * [45] Jump Game II
 */

// @lc code=start
class Solution
{
public:
    int jump(vector<int> &nums)
    {
        int end, far, jumps;
        end = far = jumps = 0;

        for (int i = 0; i < nums.size(); ++i)
        {
            if (i > end)
            {
                jumps++;
                end = far;
            }
            far = max(far, i + nums[i]);
        }

        return jumps;
    }
};
// @lc code=end
