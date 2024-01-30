/*
 * @lc app=leetcode id=121 lang=cpp
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
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
// @lc code=end

