#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy_price = INT_MAX, max_profit = 0;

        for (const int &p : prices)
        {
          if (p < buy_price)
          {
            buy_price = p;
          }
          else
          {
            max_profit = max(max_profit, p - buy_price);
          }
        }

        return max_profit;
    }
};