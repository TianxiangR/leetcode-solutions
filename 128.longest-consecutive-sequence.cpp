/*
 * @lc app=leetcode id=128 lang=cpp
 *
 * [128] Longest Consecutive Sequence
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        unordered_set<int> exist(begin(nums), end(nums));
        int answer = 0;
        for (int n : nums)
        {
            if (!exist.count(n - 1))
            {
                int curr_num = n;
                int curr_length = 1;

                while (exist.count(curr_num + 1))
                {
                    curr_length++;
                    curr_num++;
                }

                answer = max(answer, curr_length);
            }
        }

        return answer;
    }
};
// @lc code=end
