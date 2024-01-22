#include <bits/stdc++.h>

using namespace std;


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