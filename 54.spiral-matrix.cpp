/*
 * @lc app=leetcode id=54 lang=cpp
 *
 * [54] Spiral Matrix
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
enum Direction
{
    RIGHT,
    DOWN,
    LEFT,
    UP
};

class Solution
{
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix)
    {
        int row_index = 0, col_index = 0, step_count = 0,
            matrix_size = matrix.size() * matrix[0].size(),
            up_bound = 1, left_bound = 0, right_bound = matrix[0].size() - 1, down_bound = matrix.size() - 1;

        Direction next_move = RIGHT;
        vector<int> answer;

        while (step_count < matrix_size)
        {
            int curr_val = matrix[row_index][col_index];
            answer.push_back(curr_val);
            switch (next_move)
            {
            case RIGHT:
                if (col_index == right_bound)
                {
                    next_move = DOWN;
                    right_bound--;
                    row_index++;
                }
                else
                {
                    col_index++;
                }
                break;
            case DOWN:
                if (row_index == down_bound)
                {
                    next_move = LEFT;
                    down_bound--;
                    col_index--;
                }
                else
                {
                    row_index++;
                }
                break;
            case LEFT:
                if (col_index == left_bound)
                {
                    next_move = UP;
                    left_bound++;
                    row_index--;
                }
                else
                {
                    col_index--;
                }
                break;
            case UP:
                if (row_index == up_bound)
                {
                    next_move = RIGHT;
                    up_bound++;
                    col_index++;
                }
                else
                {
                    row_index--;
                }
                break;
            }
            step_count++;
        }

        return answer;
    }
};
// @lc code=end

int main()
{
    Solution s;
    vector<vector<int>> input = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    s.spiralOrder(input);
}
