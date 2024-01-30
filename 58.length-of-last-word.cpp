/*
 * @lc app=leetcode id=58 lang=cpp
 *
 * [58] Length of Last Word
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution
{
public:
    int lengthOfLastWord(string s)
    {
        int word_len = 0, input_len = s.size();

        for (int i = 0; i < input_len; ++i)
        {
            char c = s[i];

            if (c != ' ')
            {
                if (i == 0 || s[i - 1] != ' ')
                    word_len++;
                else
                    word_len = 1;
            }
        }

        return word_len;
    }
};
// @lc code=end
