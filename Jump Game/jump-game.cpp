#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int max_length = 0;

        for (int i = 0; i < nums.size(); ++i)
        {
            if (max_length >= i)
            {
                max_length = max(max_length, i + nums[i]);
            }
            else
            {
                return false;
            }
        }

        return true;
    }
};