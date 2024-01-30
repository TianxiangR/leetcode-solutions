/*
 * @lc app=leetcode id=189 lang=cpp
 *
 * [189] Rotate Array
 */
#include <bits/stdc++.h>

using namespace std;
// @lc code=start
class Solution
{
public:
    void rotate(vector<int> &nums, int k)
    {
        int n = nums.size(), count = 0;
        k = k % n;

        for (int start = 0; count < n; start++)
        {
            int current = start, prev = nums[start];
            do
            {
                int next = (current + k) % n;
                int temp = nums[next];
                nums[next] = prev;
                prev = temp;
                current = next;
                count++;
            } while (start != current);
        }
    }
};
// @lc code=end
