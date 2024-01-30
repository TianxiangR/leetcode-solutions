/*
 * @lc app=leetcode id=22 lang=cpp
 *
 * [22] Generate Parentheses
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution
{
private:
    unordered_map<int, vector<string>> dp;

public:
    Solution()
    {
        dp[0] = {""};
    }

    vector<string> generateParenthesis(int n)
    {
        if (dp.find(n) != dp.end())
        {
            return dp[n];
        }

        vector<string> answer;

        for (int i = 1; i <= n; ++i)
        {
            vector<string> left = generateParenthesis(i - 1), right = generateParenthesis(n - i);

            for (auto l : left)
            {
                for (auto r : right)
                {
                    answer.push_back("(" + l + ")" + r);
                }
            }
        }

        dp[n] = answer;
        return answer;
    }
};
// @lc code=end

int main()
{
    Solution s;
    s.generateParenthesis(3);
}
