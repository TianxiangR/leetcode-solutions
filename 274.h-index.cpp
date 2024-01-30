/*
 * @lc app=leetcode id=274 lang=cpp
 *
 * [274] H-Index
 */

// @lc code=start
class Solution
{
public:
    int hIndex(vector<int> &citations)
    {
        sort(citations.begin(), citations.end(), greater<int>());
        int h = 0;

        for (int i = 0; i < citations.size(); i++)
        {
            if (citations[i] > h)
                h++;
            else
                break;
        }

        return h;
    }
};
// @lc code=end
