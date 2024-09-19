/*
 * @lc app=leetcode id=49 lang=cpp
 *
 * [49] Group Anagrams
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
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        unordered_map<string, vector<string>> map;

        for (string &s : strs)
        {
            string copy(s);
            sort(begin(copy), end(copy));

            map[copy] = getOrDefault(map, copy, {});
            map[copy].push_back(s);
        }

        vector<vector<string>> answer;
        for (auto p : map)
        {
            answer.push_back(p.second);
        }

        return answer;
    }
};
// @lc code=end
