/*
 * @lc app=leetcode id=3 lang=cpp
 *
 * [3] Longest Substring Without Repeating Characters
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_set<char> seen;
        int p = 0, q = 0, answer = 0;

        while (p <= q && q < size(s))
        {
            if (seen.count(s[q]))
            {
                while (seen.count(s[q]))
                {
                    seen.erase(s[p++]);
                }
            }
            else
            {
                seen.insert(s[q++]);
            }

            answer = max(answer, static_cast<int>(seen.size()));
        }

        return answer;
    }
};
// @lc code=end
