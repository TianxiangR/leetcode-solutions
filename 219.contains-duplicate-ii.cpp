/*
 * @lc app=leetcode id=219 lang=cpp
 *
 * [219] Contains Duplicate II
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    bool containsNearbyDuplicate(vector<int> &nums, int k)
    {
        unordered_map<int, vector<int>> map;

        for (int i = 0; i < nums.size(); ++i)
        {
            map[nums[i]].push_back(i);
        }

        for (auto p : map)
        {
            for (int i = 1; i < p.second.size(); ++i)
            {
                if (p.second[i] - p.second[i - 1] <= k)
                {
                    return true;
                }
            }
        }

        return false;
    }
};
// @lc code=end
