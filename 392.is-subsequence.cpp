/*
 * @lc app=leetcode id=392 lang=cpp
 *
 * [392] Is Subsequence
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        if (s.size() == 0)
            return true;

        int j = 0;

        for (int i = 0; i < t.size(); ++i)
        {
            if (s[j] == t[i])
            {
                j++;
            }

            if (j == s.size())
            {
                return true;
            }
        }

        return false;
    }
};
// @lc code=end
