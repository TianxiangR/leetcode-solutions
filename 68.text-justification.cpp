/*
 * @lc app=leetcode id=68 lang=cpp
 *
 * [68] Text Justification
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
private:
    string justifyNormalLines(vector<string> &words, int maxWidth)
    {
        string output = words[0];
        int total_word_length = 0, white_space_length, padding_num = max(words.size() - 1, static_cast<size_t>(1));
        for (auto word : words)
        {
            total_word_length += word.size();
        }

        white_space_length = maxWidth - total_word_length;

        string padding = "";
        int padding_length = white_space_length / padding_num;
        int remainder = white_space_length % padding_num;

        for (int i = 0; i < padding_length; ++i)
            padding += ' ';

        if (words.size() == 1)
        {
            return output + padding;
        }

        for (int i = 1; i < words.size(); ++i)
        {
            if (i <= remainder)
            {
                output += ' ';
            }
            output += padding + words[i];
        }

        return output;
    }

    string justifyLastLine(vector<string> &words, int maxWidth)
    {
        string output = words[0];

        for (int i = 1; i < words.size(); ++i)
        {
            output += " " + words[i];
        }

        int remaining_space = maxWidth - output.size();

        for (int i = 0; i < remaining_space; ++i)
        {
            output += ' ';
        }

        return output;
    }

public:
    vector<string> fullJustify(vector<string> &words, int maxWidth)
    {
        vector<string> answer;
        int line_length = 0;
        vector<vector<string>> lines;
        vector<string> line;
        for (int i = 0; i < words.size(); ++i)
        {
            string word = words[i];
            int next_line_length = line_length == 0 ? word.size() : line_length + word.size() + 1;
            if (next_line_length <= maxWidth)
            {
                if (line_length != 0)
                {
                    line_length++;
                }
                line_length += word.size();
                line.push_back(word);
            }
            else
            {
                lines.push_back(line);
                line = {word};
                line_length = word.size();
            }
        }

        for (auto l : lines)
        {
            answer.push_back(justifyNormalLines(l, maxWidth));
        }

        answer.push_back(justifyLastLine(line, maxWidth));

        return answer;
    }
};
// @lc code=end

int main()
{
    Solution s;
    vector<string> input = {"What", "must", "be", "acknowledgment", "shall", "be"};
    vector<string> output;

    output = s.fullJustify(input, 16);

    return 0;
}
