/*
 * @lc app=leetcode id=42 lang=cpp
 *
 * [42] Trapping Rain Water
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    int trap(vector<int> &height)
    {
        vector<int> left_dp, right_dp(height.size());
        int left_max = 0, right_max = 0, answer = 0;

        for (int i = height.size() - 1; i >= 0; --i)
        {
            int h = height[i];

            if (h > right_max)
            {
                right_max = h;
                right_dp[i] = 0;
            }
            else
            {
                right_dp[i] = right_max - h;
            }
        }

        for (int i = 0; i < height.size(); ++i)
        {
            int h = height[i];

            if (h > left_max)
            {
                left_max = h;
                left_dp.push_back(0);
            }
            else
            {
                left_dp.push_back(left_max - h);
            }

            answer += min(left_dp[i], right_dp[i]);
        }

        return answer;
    }
};
// @lc code=end
