/*
 * @lc app=leetcode id=290 lang=cpp
 *
 * [290] Word Pattern
 */

#include <bits/stdc++.h>
using namespace std;
// @lc code=start
vector<string> splitString(const string &s, const char &delim)
{
    vector<string> output;
    string buffer;

    for (const char &c : s)
    {
        if (c == delim && buffer.size() != 0)
        {
            output.push_back(buffer);
            buffer = "";
        }
        else if (c != delim)
        {
            buffer.push_back(c);
        }
    }

    if (buffer.size() != 0)
    {
        output.push_back(buffer);
    }

    return output;
}

class Solution
{
public:
    bool wordPattern(string pattern, string s)
    {
        unordered_map<char, string> c_to_s;
        unordered_map<string, char> s_to_c;

        vector<string> strs = splitString(s, ' ');

        if (strs.size() != pattern.size())
        {
            return false;
        }

        for (int i = 0; i < pattern.size(); ++i)
        {
            const char &c = pattern[i];
            const string &str = strs[i];

            if (c_to_s.find(c) != c_to_s.end() && c_to_s[c] != str)
            {
                return false;
            }
            if (s_to_c.find(str) != s_to_c.end() && s_to_c[str] != c)
            {
                return false;
            }

            c_to_s[c] = str;
            s_to_c[str] = c;
        }

        return true;
    }
};
// @lc code=end

int main()
{
    Solution s;
    s.wordPattern("abba", "dog dog dog dog");
    return 0;
}
