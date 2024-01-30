/*
 * @lc app=leetcode id=383 lang=cpp
 *
 * [383] Ransom Note
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
    bool canConstruct(string ransomNote, string magazine)
    {
        unordered_map<char, int> map;

        for (const char &c : magazine)
        {
            map[c] = getOrDefault(map, c, 0) + 1;
        }

        for (const char &c : ransomNote)
        {
            if (!getOrDefault(map, c, 0))
            {
                return false;
            }
            map[c]--;
        }

        return true;
    }
};
// @lc code=end
