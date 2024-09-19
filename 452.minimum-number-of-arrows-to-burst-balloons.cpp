/*
 * @lc app=leetcode id=452 lang=cpp
 *
 * [452] Minimum Number of Arrows to Burst Balloons
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
bool isIntersected(const vector<int> &a, const vector<int> &b)
{
    return (b[0] <= a[0] && a[0] <= b[1]) || (a[0] <= b[0] && b[0] <= a[1]);
}

int compareIntervals(const vector<int> &a, const vector<int> &b)
{
    if (a[1] == b[1])
    {
        long long diff = (long long)a[0] - (long long)b[0];
        if (diff < 0)
        {
            diff = -1;
        }
        else if (diff > 0)
        {
            diff = 1;
        }
        return diff;
    }

    long long diff = (long long)a[1] - (long long)b[1];
    if (diff < 0)
    {
        diff = -1;
    }
    else if (diff > 0)
    {
        diff = 1;
    }
    return diff;
}

bool compare(const vector<int> &a, const vector<int> &b)
{
    return compareIntervals(a, b) < 0;
}

class Solution
{
public:
    int findMinArrowShots(vector<vector<int>> &points)
    {
        int answer = 0;
        sort(begin(points), end(points), compare);
        for (int i = 0; i < size(points); ++i)
        {
            auto current = points[i];

            while (i + 1 < size(points) && isIntersected(current, points[i + 1]))
            {
                ++i;
            }

            answer++;
        }

        return answer;
    }
};
// @lc code=end
