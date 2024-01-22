#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
  vector<int> productExceptSelf(vector<int> &nums)
  {
    int len = nums.size();
    vector<int> ans(len);

    int left = 1, right = 1;
    ans[0] = left;
    for (int i = 1; i < len; ++i)
    {
      left *= nums[i - 1];
      ans[i] = left;
    }

    for (int i = len - 2; i >= 0; --i)
    {
      right *= nums[i + 1];
      ans[i] *= right;
    }

    return ans;
  }
};

int main()
{
  vector<int> input = {1, 2, 3, 4};
  Solution s;

  vector<int> ans = s.productExceptSelf(input);


  return 0;
}