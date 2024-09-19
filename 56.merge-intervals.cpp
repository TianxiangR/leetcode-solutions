/*
 * @lc app=leetcode id=56 lang=cpp
 *
 * [56] Merge Intervals
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
bool compare(const vector<int> &a, const vector<int> &b)
{
    if (a[0] == b[0])
    {
        return a[1] < b[1];
    }

    return a[0] < b[0];
}

class Solution
{
public:
    vector<vector<int>> merge(vector<vector<int>> &intervals)
    {
        sort(begin(intervals), end(intervals), compare);
        vector<int> curr_interval = intervals[0];
        vector<vector<int>> answer;

        for (int i = 1; i < intervals.size(); ++i)
        {
            if (curr_interval[1] >= intervals[i][0])
            {
                curr_interval[1] = max(curr_interval[1], intervals[i][1]);
            }
            else
            {
                answer.push_back(curr_interval);
                curr_interval = intervals[i];
            }
        }

        answer.push_back(curr_interval);

        return answer;
    }
};
// @lc code=end

int main()
{
    Solution s;
    vector<vector<int>> input = {{0, 3}, {1, 1}}, output = s.merge(input);

    return 0;
}
