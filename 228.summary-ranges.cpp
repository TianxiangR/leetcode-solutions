/*
 * @lc app=leetcode id=228 lang=cpp
 *
 * [228] Summary Ranges
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
string intervalToString(pair<int, int> interval)
{
    if (interval.first == interval.second)
    {
        return to_string(interval.first);
    }

    return to_string(interval.first) + "->" + to_string(interval.second);
}

class Solution
{
public:
    vector<string> summaryRanges(vector<int> &nums)
    {
        if (!size(nums))
        {
            return {};
        }

        int start = nums[0];
        vector<pair<int, int>> intervals;

        for (int i = 1; i < size(nums); ++i)
        {
            if (nums[i] != nums[i - 1] + 1)
            {
                intervals.push_back({start, nums[i - 1]});
                start = nums[i];
            }
        }

        intervals.push_back({start, nums.back()});

        vector<string> answer;

        for (auto itvl : intervals)
        {
            answer.push_back(intervalToString(itvl));
        }

        return answer;
    }
};
// @lc code=end

int main()
{
    
}