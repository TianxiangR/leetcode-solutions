#include <bits/stdc++.h>
using namespace std;

vector<string> splitString(const string &s, const char &delim)
{
  vector<string> output;
  string buffer;

  for (const char &c : s)
  {
    if (c == delim && buffer.size() != 0)
    {
      output.push_back(buffer);
      buffer = "";
    }
    else if (c != delim)
    {
      buffer.push_back(c);
    }
  }

  if (buffer.size() != 0)
  {
    output.push_back(buffer);
  }

  return output;
}

template <typename T, typename P>
P getOrDefault(const unordered_map<T, P> &map, const T &key, const P &default_value)
{
  if (map.find(key) != map.end())
  {
    return map.at(key);
  }

  return default_value;
}

vector<int> mergeIntervals(const vector<int> &a, const vector<int> &b)
{
  return {min(a[0], b[0]), max(a[1], b[1])};
}

bool isIntersected(const vector<int> &a, const vector<int> &b)
{
  return (b[0] <= a[0] && a[0] <= b[1]) || (a[0] <= b[0] && b[0] <= a[1]);
}

int compareIntervals(const vector<int> &a, const vector<int> &b)
{
  if (a[0] == b[0])
    return a[1] - b[1];

  return a[0] - b[0];
}

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

template <typename T>
inline T &queue_pop(queue<T> &q)
{
  T &rval = q.front();
  q.pop();
  return rval;
}

template <typename T>
inline T &stack_pop(stack<T> &s)
{
  T &rval = s.top();
  s.pop();
  return rval;
}

template <typename T>
bool isLeaf(T *node)
{
  return node->left == NULL && node->right == NULL;
}

template <typename T>
bool istail(T *node)
{
  return node->next == NULL;
}