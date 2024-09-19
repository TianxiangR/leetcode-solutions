/*
 * @lc app=leetcode id=345 lang=cpp
 *
 * [345] Reverse Vowels of a String
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    string reverseVowels(string s)
    {
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int p = 0, q = s.size() - 1;
        bool find_left_vowel = true;

        while (p < q)
        {
            if (find_left_vowel)
            {
                if (vowels.find(s[p]) != end(vowels))
                {
                    find_left_vowel = !find_left_vowel;
                }
                else
                {
                    p++;
                }
            }
            else
            {
                if (vowels.find(s[q]) != end(vowels))
                {
                    // swap
                    swap(s[p], s[q]);
                    p++;
                    q--;
                    find_left_vowel = !find_left_vowel;
                }
                else
                {
                    q--;
                }
            }
        }

        return s;
    }
};
// @lc code=end
