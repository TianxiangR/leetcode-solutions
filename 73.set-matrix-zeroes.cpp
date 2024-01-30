/*
 * @lc app=leetcode id=73 lang=cpp
 *
 * [73] Set Matrix Zeroes
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    void setZeroes(vector<vector<int>> &matrix)
    {
        bool isCol = false;

        for (int i = 0; i < matrix.size(); ++i)
        {
            for (int j = 0; j < matrix[0].size(); ++j)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }

                if (j == 0)
                {
                    isCol = true;
                }
            }
        }

        for (int i = 1; i < matrix.size(); ++i)
        {
            for (int j = 1; j < matrix[0].size(); ++j)
            {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                {
                    matrix[i][j] = 0;
                }
            }
        }

        if (matrix[0][0] == 0)
        {
            for (int i = 1; i < matrix.size(); ++i)
            {
                matrix[0][i] = 0;
            }
        }

        if (isCol)
        {
            for (int i = 1; i < matrix[0].size(); ++i)
            {
                matrix[i][0] = 0;
            }
        }
    }
};
// @lc code=end
int main()
{
    Solution s;
    vector<vector<int>> input = {{1, 1, 1, 1}, {1, 0, 1, 1}, {1, 1, 0, 0}, {0, 0, 0, 1}};
    s.setZeroes(input);

    return 0;
}