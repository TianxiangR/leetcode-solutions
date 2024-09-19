/*
 * @lc app=leetcode id=242 lang=cpp
 *
 * [242] Valid Anagram
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
template <typename T, typename P>
P getOrDefault(const unordered_map<T, P> &map, const T &key, const P &default_value)
{
    if (map.find(key) != map.end())
    {
        return map.at(key);
    }

    return default_value;
}

class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        if (s.size() != t.size())
        {
            return false;
        }

        unordered_map<char, int> map;

        for (char &c : s)
        {
            map[c] = getOrDefault(map, c, 0) + 1;
        }

        for (char &c : t)
        {
            if (getOrDefault(map, c, 0))
            {
                map[c]--;
            }
            else
            {
                return false;
            }
        }

        return true;
    }
};
// @lc code=end
