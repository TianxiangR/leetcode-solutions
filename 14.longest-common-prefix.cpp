/*
 * @lc app=leetcode id=14 lang=cpp
 *
 * [14] Longest Common Prefix
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        size_t shortest_len = strs[0].size();
        string answer = "";

        for (auto s : strs)
            shortest_len = min(shortest_len, s.size());

        for (size_t i = 0; i < shortest_len; ++i)
        {
            bool all_equal = true;
            char curr_c = strs[0][i];

            for (auto s : strs)
            {
                if (s[i] != curr_c)
                {
                    all_equal = false;
                    break;
                }
            }

            if (all_equal)
            {
                answer += curr_c;
            }
            else
            {
                break;
            }
        }

        return answer;
    }
};
// @lc code=end
