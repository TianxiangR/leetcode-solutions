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
        unordered_set<int> dup;
        set<tuple<int, int, int>> res;

        for (int i; i < nums.size(); ++i)
        {
            int i_val = nums[i];

            if (dup.find(i_val) != end(dup))
            {
                continue;
            }

            unordered_set<int> *seen = new unordered_set<int>();

            for (int j = i + 1; j < nums.size(); ++j)
            {
                int j_val = nums[j];
                int complement = -i_val - j_val;
                if (seen->find(j_val) != seen->end())
                {
                    vector<int> triplet = {i_val, j_val, complement};
                    sort(begin(triplet), end(triplet));
                    tuple<int, int, int> tp = {triplet[0], triplet[1], triplet[2]};
                    res.insert(tp);
                }
                seen->insert(j_val);
            }

            delete seen;
        }

        return vector<vector<int>>(begin(res))
    }
};
// @lc code=end
