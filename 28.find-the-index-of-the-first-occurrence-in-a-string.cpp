/*
 * @lc app=leetcode id=28 lang=cpp
 *
 * [28] Find the Index of the First Occurrence in a String
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;

// prefix table for KMP
using vi = vector<int>;
vi pi(const string &s)
{
    vector<int> p(s.size(), 0);
    for (int i = 1, g = 0; i < s.size(); g = p[i++])
    {
        while (g && s[i] != s[g])
            g = p[g - 1];
        p[i] = g + (s[i] == s[g]);
    }
    return p;
}

class Solution
{
public:
    int strStr(string haystack, string needle)
    {
        vi p = pi(needle + "#" + haystack);
        for (int i = needle.size() + 1; i < p.size(); ++i)
        {
            if (p[i] == needle.size())
            {
                return i - needle.size() - needle.size();
            }
        }

        return -1;
    }
};
// @lc code=end

int main()
{
    Solution s;

    s.strStr("mississippi", "issip");

    return 0;
}
