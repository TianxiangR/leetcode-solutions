/*
 * @lc app=leetcode id=1657 lang=cpp
 *
 * [1657] Determine if Two Strings Are Close
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    bool closeStrings(string word1, string word2)
    {
        vector<int> freq1(26, 0), freq2(26, 0);

        for (const char &c : word1)
        {
            freq1[c - 'a']++;
        }
        for (const char &c : word2)
        {
            freq2[c - 'a']++;
        }

        for (int i = 0; i < 26; ++i)
        {
            bool has1, has2;
            has1 = (bool)freq1[i];
            has2 = (bool)freq2[i];

            if (has1 ^ has2)
            {
                return false;
            }
        }

        sort(begin(freq1), end(freq1));
        sort(begin(freq2), end(freq2));

        return freq1 == freq2;
    }
};
// @lc code=end
