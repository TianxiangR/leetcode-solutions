/*
 * @lc app=leetcode id=289 lang=cpp
 *
 * [289] Game of Life
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start

bool is_valid_indices(vector<vector<int>> &board, int a, int b)
{
    return 0 <= a && a < board.size() && 0 <= b && b < board[0].size();
}

bool is_alive_before(vector<vector<int>> &board, int a, int b)
{
    return board[a][b] & 1;
}

bool is_alive_after(vector<vector<int>> &board, int a, int b)
{
    return board[a][b] & 2;
}
class Solution
{
public:
    void gameOfLife(vector<vector<int>> &board)
    {
        for (int i = 0; i < board.size(); ++i)
        {
            for (int j = 0; j < board[0].size(); ++j)
            {
                int neighbors_alive = 0;
                vector<pair<int, int>> neighbors = {{i - 1, j - 1}, {i - 1, j}, {i - 1, j + 1}, {i, j - 1}, {i, j + 1}, {i + 1, j - 1}, {i + 1, j}, {i + 1, j + 1}};
                for (auto neighbor : neighbors)
                {
                    if (is_valid_indices(board, neighbor.first, neighbor.second))
                    {
                        neighbors_alive += is_alive_before(board, neighbor.first, neighbor.second);
                    }
                }

                if (is_alive_before(board, i, j))
                {
                    if (neighbors_alive == 2 || neighbors_alive == 3)
                    {
                        board[i][j] += 2;
                    }
                }
                else
                {
                    if (neighbors_alive == 3)
                    {
                        board[i][j] += 2;
                    }
                }
            }
        }

        for (int i = 0; i < board.size(); ++i)
        {
            for (int j = 0; j < board[0].size(); ++j)
            {
                if (is_alive_after(board, i, j))
                {
                    board[i][j] = 1;
                }
                else
                {
                    board[i][j] = 0;
                }
            }
        }
    }
};
// @lc code=end

int main()
{
    vector<vector<int>> board = {{0, 1}};
    cout << is_alive_after(board, 0, 1) << endl;
}