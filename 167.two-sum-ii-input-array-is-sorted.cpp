/*
 * @lc app=leetcode id=167 lang=cpp
 *
 * [167] Two Sum II - Input Array Is Sorted
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        int low = 0;
        int high = numbers.size() - 1;

        while (low < high)
        {
            int sum = numbers[low] + numbers[high];

            if (sum == target)
            {
                return {low + 1, high + 1};
            }
            else if (sum < target)
            {
                low++;
            }
            else
            {
                high--;
            }
        }

        return {-1, -1};
    }
};
// @lc code=end
