/*
 * @lc app=leetcode id=57 lang=cpp
 *
 * [57] Insert Interval
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
vector<int> mergeIntervals(const vector<int> &a, const vector<int> &b)
{
    return {min(a[0], b[0]), max(a[1], b[1])};
}

bool isIntersected(const vector<int> &a, const vector<int> &b)
{
    return (b[0] <= a[0] && a[0] <= b[1]) || (a[0] <= b[0] && b[0] <= a[1]);
}

int compareIntervals(const vector<int> &a, const vector<int> &b)
{
    if (a[0] == b[0])
        return a[1] - b[1];

    return a[0] - b[0];
}

class Solution
{
public:
    vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval)
    {
        vector<vector<int>> answer;
        bool inserted = false;

        for (int i = 0; i < size(intervals); ++i)
        {
            if ((compareIntervals(newInterval, intervals[i]) <= 0 || isIntersected(newInterval, intervals[i])) && !inserted)
            {
                if (isIntersected(newInterval, intervals[i]))
                {
                    while (i < size(intervals) && isIntersected(newInterval, intervals[i]))
                    {
                        newInterval = mergeIntervals(newInterval, intervals[i]);
                        ++i;
                    }
                }

                answer.push_back(newInterval);
                inserted = true;
            }

            if (i < size(intervals))
            {
                answer.push_back(intervals[i]);
            }
        }

        if (!inserted)
        {
            // insert at the back
            answer.push_back(newInterval);
        }

        return answer;
    }
};
// @lc code=end
