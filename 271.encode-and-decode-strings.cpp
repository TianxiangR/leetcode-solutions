#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Codec
{
public:
  // Encodes a list of strings to a single string.
  string encode(vector<string> &strs)
  {
    string result;
    for (const string s : strs)
    {
      for (const char c : s)
      {
        if (c == '\\' || c == ',')
        {
          result.push_back('\\');
        }
        result.push_back(c);
      }
      result += ',';
    }

    return result;
  }

  // Decodes a single string to a list of strings.
  vector<string> decode(string s)
  {
    vector<string> result;
    string stringBuilder;
    for (int i = 0; i < s.size(); ++i)
    {
      const char c = s[i];
      if (c == '\\' && i < s.size())
      {
        const char next = s[++i];
        switch (next)
        {
        case '\\':
        case ',':
          stringBuilder.push_back(next);
          break;
        default:
          stringBuilder.push_back(c);
          stringBuilder.push_back(next);
        }
      }
      else if (c == ',')
      {
        result.push_back(stringBuilder);
        stringBuilder = "";
      }
      else
      {
        stringBuilder.push_back(c);
      }
    }

    return result;
  }
};