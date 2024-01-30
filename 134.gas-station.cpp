/*
 * @lc app=leetcode id=134 lang=cpp
 *
 * [134] Gas Station
 */

// @lc code=start
class Solution
{
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost)
    {
        int net_gas = 0, start = 0, curr_gain = 0, total_steps = gas.size();

        for (int i = 0; i < total_steps; ++i)
        {
            net_gas += gas[i] - cost[i];
            curr_gain += gas[i] - cost[i];
            if (curr_gain < 0)
            {
                start = i + 1;
                curr_gain = 0;
            }
        }

        return net_gas >= 0 ? start : -1;
    }
};
// @lc code=end
