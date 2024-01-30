/*
 * @lc app=leetcode id=151 lang=cpp
 *
 * [151] Reverse Words in a String
 */

// @lc code=start
class Solution
{
public:
  string reverseWords(string s)
  {
    // reverse the string entirely
    size_t len = s.size(), p = 0, q = len - 1;
    while (p < q)
    {
      swap(s[p], s[q]);
      p++;
      q--;
    }

    // reverse words
    size_t start = -1, end = -1;
    for (int i = 0; i < len; ++i)
    {
      if (s[i] != ' ')
      {
        if (start == -1)
        {
          start = i;
        }

        end = i;
      }
      else
      {
        while (start != -1 && start < end)
        {
          swap(s[start], s[end]);
          start++;
          end--;
        }

        start = -1;
      }
    }

    while (start != -1 && start < end)
    {
      swap(s[start], s[end]);
      start++;
      end--;
    }

    // remove spaces
    bool remove_space = s[0] == ' ';
    int replace_index = 0;
    for (int i = 0; i < len; ++i)
    {
      if (remove_space)
      {
        while (i < len && s[i] == ' ')
        {
          ++i;
        }
        remove_space = false;
        --i;
        continue;
      }
      if (s[i] == ' ')
      {
        remove_space = true;
      }

      s[replace_index++] = s[i];
    }

    if (replace_index > 1 && s[replace_index - 1] == ' ')
    {
      return s.substr(0, replace_index - 1);
    }

    return s.substr(0, replace_index);
  }
};
// @lc code=end

