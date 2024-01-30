/*
 * @lc app=leetcode id=6 lang=cpp
 *
 * [6] Zigzag Conversion
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    string convert(string s, int numRows)
    {
        int col_size = numRows, diag_size = max(0, numRows - 2);
        int seg_size = col_size + diag_size;
        vector<string> zigzag;

        for (int i = 0; i < s.size();)
        {
            string seg;
            while (seg.size() != seg_size && i < s.size())
            {
                seg.push_back(s[i]);
                i++;
            }
            zigzag.push_back(seg);
        }

        string answer;
        for (int i = 0; i < numRows; ++i)
        {
            for (auto &seg : zigzag)
            {
                if (i < seg.size())
                {
                    answer.push_back(seg[i]);
                }

                if (i != 0 && i != numRows - 1)
                {
                    int diag_index = seg_size - i;

                    if (diag_index < seg.size())
                    {
                        answer.push_back(seg[diag_index]);
                    }
                }
            }
        }

        return answer;
    }
};
// @lc code=end
