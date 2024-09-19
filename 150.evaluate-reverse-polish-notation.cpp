/*
 * @lc app=leetcode id=150 lang=cpp
 *
 * [150] Evaluate Reverse Polish Notation
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
bool isNumeric(const string &s)
{
    if (s.size() == 0)
        return false;

    if (s.size() == 1)
        return isdigit(s[0]);

    if (!isdigit(s[0]) && s[0] != '-' && s[0] != '+')
    {
        return false;
    }

    for (int i = 1; i < size(s); ++i)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }

    return true;
}

class Solution
{
public:
    int evalRPN(vector<string> &tokens)
    {
        stack<int> stack;
        int answer;
        for (string &token : tokens)
        {
            if (isNumeric(token))
            {
                stack.push(atoi(token.c_str()));
            }
            else
            {
                int a, b;
                b = stack.top();
                stack.pop();
                a = stack.top();
                stack.pop();
                if (token == "+")
                {
                    answer = a + b;
                }
                else if (token == "-")
                {
                    answer = a - b;
                }
                else if (token == "*")
                {
                    answer = a * b;
                }
                else if (token == "/")
                {
                    answer = a / b;
                }

                stack.push(answer);
            }
        }

        return stack.top();
    }
};
// @lc code=end
int main()
{
    vector<string> input = {"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"};
    Solution s;
    cout << s.evalRPN(input) << endl;
}
