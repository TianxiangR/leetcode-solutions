/*
 * @lc app=leetcode id=205 lang=cpp
 *
 * [205] Isomorphic Strings
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    bool isIsomorphic(string s, string t)
    {
        if (s.size() != t.size())
        {
            return false;
        }

        unordered_map<char, char> s_to_t;
        unordered_map<char, char> t_to_s;

        for (int i = 0; i < s.size(); ++i)
        {
            if (s_to_t.count(s[i]) && t[i] != s_to_t[s[i]])
            {
                return false;
            }

            if (!s_to_t.count(s[i]) != !t_to_s.count(t[i]))
            {
                return false;
            }

            s_to_t[s[i]] = t[i];
            t_to_s[t[i]] = s[i];
        }

        return true;
    }
};
// @lc code=end
