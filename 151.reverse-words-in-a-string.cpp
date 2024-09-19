/*
 * @lc app=leetcode id=151 lang=cpp
 *
 * [151] Reverse Words in a String
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
  string reverseWords(string s)
  {
    // Step 1: reverse the original string
    reverse(begin(s), end(s));

    // Step 2: find the start and the end of a word and reverse it back to normal order  
    int start = -1;
    for (int i = 0; i < s.size(); ++i)
    {
      char c = s[i];
      if (c != ' ')
      {
        if (start == -1)
        {
          start = i;
        }
        if (i == s.size() - 1 || s[i + 1] == ' ')
        {
          // reverse the word
          int p = start, q = i;
          while (p < q)
          {
            swap(s[p], s[q]);
            p++;
            q--;
          }

          start = -1;
        }
      }
    }

    // Step 3: remove extra spaces
    int input_index = 0;
    for (int i = 0; i < s.size(); ++i)
    {
      if (s[i] != ' ')
      {
        if (i > 0 && s[i - 1] == ' ' && input_index > 0)
        {
          s[input_index++] = ' ';
        }

        s[input_index++] = s[i];
      }
    }

    // Step 4: remove extra chars
    while (input_index != s.size())
    {
      s.pop_back();
    }

    return s;
  }
};
// @lc code=end
