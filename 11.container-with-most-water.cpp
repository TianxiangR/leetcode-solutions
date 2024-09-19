/*
 * @lc app=leetcode id=11 lang=cpp
 *
 * [11] Container With Most Water
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int lo = 0, hi = height.size() - 1, max_area = 0;

        while (lo < hi)
        {
            int new_area = min(height[lo], height[hi]) * (hi - lo);
            max_area = max(max_area, new_area);
            if (height[lo] <= height[hi])
            {
                lo++;
            }
            else
            {
                hi--;
            }
        }

        return max_area;
    }
};
// @lc code=end

int main()
{
    Solution s;
    vector<int> input = {1, 3, 2, 5, 25, 24, 5};
    int output = s.maxArea(input);

    return 0;
}
