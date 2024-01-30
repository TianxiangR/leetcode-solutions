/*
 * @lc app=leetcode id=122 lang=cpp
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int buy_price = prices[0], profit = 0;

        for (int i = 1; i < prices.size(); ++i)
        {
            if (prices[i] < prices[i - 1])
            {
                if (prices[i - 1] - buy_price > 0)
                    profit += prices[i - 1] - buy_price;
                buy_price = prices[i];
            }
        }

        if (prices.back() - buy_price > 0)
        {
            profit += prices.back() - buy_price;
        }

        return profit;
    }
};
// @lc code=end
