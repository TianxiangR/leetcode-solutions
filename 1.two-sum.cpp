/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); ++i)
        {
            int complement = target - nums[i];

            if (seen.count(nums[i]))
            {
                return {seen[nums[i]], i};
            }
            else
            {
                seen[complement] = i;
            }
        }

        return {-1, -1};
    }
};
// @lc code=end
