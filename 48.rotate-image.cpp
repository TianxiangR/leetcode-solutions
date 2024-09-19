/*
 * @lc app=leetcode id=48 lang=cpp
 *
 * [48] Rotate Image
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
private:
    vector<int> transform(int i, int j, int start, int end)
    {
        if (i == start)
        {
            return {j, end};
        }
        else if (j == end)
        {
            return {end, end - i};
        }
        else if (i == end)
        {
            return {j, start};
        }
        return {start, end - i};
    }

public:
    void rotate(vector<vector<int>> &matrix)
    {
        int i = 0, j = 0, start = 0, end = matrix.size() - 1;

        while (start < end)
        {
            for (int k = start; k <= end; ++k)
            {
                i = k;
                j = start;
                int prev = matrix[i][j];
                for (int m = 0; m < 4; m++)
                {
                    vector<int> next_index = transform(i, j, start, end);
                    i = next_index[0];
                    j = next_index[1];
                    swap(prev, matrix[i][j]);
                }
            }
            start++;
            end--;
        }
    }
};
// @lc code=end
