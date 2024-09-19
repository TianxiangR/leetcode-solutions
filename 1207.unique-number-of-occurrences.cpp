/*
 * @lc app=leetcode id=1207 lang=cpp
 *
 * [1207] Unique Number of Occurrences
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    bool uniqueOccurrences(vector<int> &arr)
    {
        unordered_map<int, int> map;
        unordered_set<int> set;

        for (const int &num : arr)
        {
            if (map.find(num) != end(map))
            {
                map[num]++;
            }
            else
            {
                map[num] = 1;
            }
        }

        for (const pair<int, int> &key_value : map)
        {
            if (set.find(key_value.second) != end(set))
            {
                return false;
            }
            set.insert(key_value.second);
        }

        return true;
    }
};
// @lc code=end
