#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        map1 , map2 = {}, {}
        char_set1, char_set2 = set(), set()
        for c in word1:
            map1[c] = map1.get(c, 0) + 1
            char_set1.add(c)
        for c in word2:
            map2[c] = map2.get(c, 0) + 1
            char_set2.add(c)
        
        for c in char_set1:
            if c not in char_set2:
                return False
        
        count_count1, count_count2 = {}, {}
        
        for value in map1.values():
            count_count1[value] = count_count1.get(value, 0) + 1
        
        for value in map2.values():
            count_count2[value] = count_count2.get(value, 0) + 1
        
        for key, value in count_count1.items():
            if key not in count_count2:
                return False
            if count_count2[key] != value:
                return False
        
        return True
        
# @lc code=end

