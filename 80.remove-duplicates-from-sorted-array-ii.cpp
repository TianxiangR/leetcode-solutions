/*
 * @lc app=leetcode id=80 lang=cpp
 *
 * [80] Remove Duplicates from Sorted Array II
 */

// @lc code=start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int p = 0, prev = INT_MIN, count = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != prev) {
                nums[p] = nums[i];
                p++;
                prev = nums[i];
                count = 1;
            } else if (count < 2) {
                nums[p] = nums[i];
                p++;
                count++;
            }
        }
      
      return p;
    }
};
// @lc code=end

