/*
 * @lc app=leetcode id=71 lang=cpp
 *
 * [71] Simplify Path
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    string simplifyPath(string path)
    {
        vector<string> nodes;
        for (int i = 0; i < size(path); ++i)
        {
            if (path[i] == '/')
            {
                string name = "";
                while (i + 1 < size(path) && path[i + 1] != '/')
                {
                    name += path[++i];
                }

                if (name == "..")
                {
                    if (nodes.size() > 0)
                    {
                        nodes.pop_back();
                    }
                }
                else if (name == ".")
                {
                    /* no-op */
                }
                else if (name == "")
                {
                    /* no-op */
                }
                else
                {
                    nodes.push_back(name);
                }
            }
        }

        if (nodes.size() == 0)
        {
            return "/";
        }

        string answer = "";
        for (string node : nodes)
        {
            answer += "/" + node;
        }

        return answer;
    }
};
// @lc code=end
