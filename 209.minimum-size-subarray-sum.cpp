/*
 * @lc app=leetcode id=209 lang=cpp
 *
 * [209] Minimum Size Subarray Sum
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution
{
public:
    int minSubArrayLen(int target, vector<int> &nums)
    {
        // compute prefix_sum
        vector<long long> prefix_sum;
        long long curr_sum = 0;
        prefix_sum.push_back(curr_sum);
        for (int i = 0; i < nums.size(); ++i)
        {
            prefix_sum.push_back(curr_sum += nums[i]);
        }

        // two pointers to find the answer
        int lo = 0, hi = 0, answer = INT_MAX;
        while (lo <= hi && hi < nums.size())
        {
            long long sum = prefix_sum[hi + 1] - prefix_sum[lo];
            if (sum >= target)
            {
                answer = min(answer, hi - lo + 1);
                lo++;
            }
            else
            {
                hi++;
            }
        }

        return answer == INT_MAX ? 0 : answer;
    }
};
// @lc code=end
