/*
 * @lc app=leetcode id=202 lang=cpp
 *
 * [202] Happy Number
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    bool isHappy(int n)
    {
        unordered_set<int> seen;

        while (1)
        {
            if (n == 1)
            {
                return true;
            }

            if (seen.count(n))
            {
                return false;
            }

            int copy = n;
            int digit_square_sum = 0;

            while (copy > 0)
            {
                int digit = copy % 10;
                digit_square_sum += digit * digit;
                copy /= 10;
            }
            seen.insert(n);
            n = digit_square_sum;
        }

        return false;
    }
};
// @lc code=end
