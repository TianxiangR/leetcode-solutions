/*
 * @lc app=leetcode id=224 lang=cpp
 *
 * [224] Basic Calculator
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
bool isNumeric(const string &s)
{
    if (s.size() == 0)
        return false;

    for (const char &c : s)
    {
        if (!isdigit(c))
            return false;
    }

    return true;
}

class Operand
{
public:
    virtual int eval() const { return 0; };
};

class NumericOperand : public Operand
{
private:
    int value;

public:
    NumericOperand(int v) : value(v){};
    int eval() const final;
};

int NumericOperand::eval() const { return value; }

class NestedOperand : public Operand
{
private:
    vector<Operand> operands;
    vector<char> operators;

public:
    NestedOperand() {}
    NestedOperand(Operand op) : operands({op}) {}
    int eval() const final;
    void add_operand(Operand op)
    {
        operands.push_back(op);
    }

    void add_operator(char c)
    {
        operators.push_back(c);
    }
};

int NestedOperand::eval() const
{
    if (size(operands) == size(operators))
    {
        int output = 0;

        for (int i = 0; i < size(operands); ++i)
        {
            if (operators[i] == '+')
            {
                output += operands[i].eval();
            }
            else
            {
                output -= operands[i].eval();
            }
        }

        return output;
    }

    if (size(operands) - 1 == size(operators))
    {
        int output = operands[0].eval();

        for (int i = 1; i < size(operands); ++i)
        {
            if (operators[i - 1] == '+')
            {
                output += operands[i].eval();
            }
            else
            {
                output -= operands[i].eval();
            }
        }

        return output;
    }

    return 0;
}

class Solution
{
public:
    int calculate(string s)
    {
        stack<NestedOperand> stack;
        NestedOperand base = NestedOperand();
        stack.push(base);

        for (int i = 0; i < s.size(); ++i)
        {
            string c = {s[i]};
            auto &top = stack.top();

            if (isNumeric(c))
            {
                while (i + 1 < s.size() && isdigit(s[i + 1]))
                {
                    c += s[i + 1];
                    ++i;
                }
                top.add_operand(NumericOperand(atoi(c.c_str())));
            }
            else if (c == "+" || c == "-")
            {
                top.add_operator(c[0]);
            }
            else if (c == "(")
            {
                stack.push(NestedOperand());
            }
            else if (c == ")")
            {
                int val = top.eval();
                stack.pop();
                auto &new_top = stack.top();
                new_top.add_operand(NumericOperand(val));
            }
        }

        return stack.top().eval();
    }
};
// @lc code=end

int main()
{
    Solution s;
    cout << s.calculate("1 + 1") << endl;
    return 0;
}
