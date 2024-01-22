#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int counter1 = 1, counter2 = 0, candidate1 = nums[0], half =  nums.size() % 2 == 0 ? nums.size() / 2 : nums.size() / 2 + 1, candidate2 = 0;

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == candidate1) {
                counter1++;
            } else {
                counter2++;
                candidate2 = nums[i];
            }
            if (counter1 >= half) {
                return candidate1;
            } 
            if (counter2 >= half) {
                return candidate2;
            }
        }

        return candidate1;
    }
};