/*
 * @lc app=leetcode id=155 lang=cpp
 *
 * [155] Min Stack
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class MinStack
{
private:
    stack<pair<int, int>> stack;

public:
    MinStack()
    {
    }

    void push(int val)
    {
        if (stack.size() == 0)
        {
            stack.push({val, val});
        }
        else
        {
            stack.push({val, min(stack.top().second, val)});
        }
    }

    void pop()
    {
        stack.pop();
    }

    int top()
    {
        return stack.top().first;
    }

    int getMin()
    {
        return stack.top().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
// @lc code=end
