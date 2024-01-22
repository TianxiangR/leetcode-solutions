#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
  int candy(vector<int> &ratings)
  {
    int size = ratings.size();
    vector<int> candies(size, 1);

    for (int i = 1; i < size; ++i)
    {
      if (ratings[i] > ratings[i - 1])
      {
        candies[i] = candies[i - 1] + 1;
      }
    }

    for (int i = size - 2; i >= 0; --i)
    {
      if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1])
      {
        candies[i] = candies[i + 1] + 1;
      }
    }

    int ans = 0;

    for (const int &can : candies)
    {
      ans += can;
    }

    return ans;
  }
};

int main()
{
  vector<int> input = {1, 0, 2};
  Solution s;
  cout << s.candy(input) << endl;
}