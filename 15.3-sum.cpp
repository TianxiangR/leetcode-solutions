/*
 * @lc app=leetcode id=15 lang=cpp
 *
 * [15] 3Sum
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        sort(begin(nums), end(nums));
        unordered_map<int, int> seen;
        vector<vector<int>> res;

        for (int i = 0; i + 2 < nums.size(); ++i)
        {
            for (int j = i + 1; j < nums.size(); ++j)
            {
                int complement = -nums[i] - nums[j];
                if (seen.count(complement) && seen[complement] >= i)
                {
                    vector<int> comb = {nums[i], complement, nums[j]};
                    sort(begin(comb), end(comb));
                    res.push_back(comb);
                }
                else
                {
                    seen[nums[j]] = i;
                }

                while (j + 1 < nums.size() && nums[j] == nums[j + 1])
                {
                    j++;
                }
            }
        }

        return res;
    }
};
// @lc code=end
