#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int end, far, jumps;
        end = far = jumps = 0;

        for (int i = 0; i < nums.size(); ++i)
        {
          if (i > end)
          {
            jumps++;
            end = far;
          }
          far = max(far, i + nums[i]);
        }

        return jumps;
    }
};