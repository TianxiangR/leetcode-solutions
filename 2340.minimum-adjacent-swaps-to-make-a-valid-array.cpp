#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
  int minimumSwaps(vector<int> &nums)
  {
    int smallest = nums.front(),
        largest = nums.back(),
        first_small_index = 0,
        first_large_index = nums.size() - 1;

    for (int i = 0; i < nums.size(); ++i)
    {
      if (nums[i] < smallest)
      {
        smallest = nums[i];
        first_small_index = i;
      }

      if (nums[nums.size() - 1 - i] > largest)
      {
        largest = nums[nums.size() - 1 - i];
        first_large_index = nums.size() - 1 - i;
      }
    }

    return first_small_index + nums.size() - 1 - first_large_index - (int)(first_small_index > first_large_index);
  }
};