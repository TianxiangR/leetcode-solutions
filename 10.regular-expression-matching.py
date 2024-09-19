#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start

cache = {}

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p1, p2 = 0, 0
        current_matching = None
        pre_matching = None
        
        while p1 < len(s) or p2 < len(p):
            if p2 < len(p):
                if p[p2] == '.' or p[p2].isalpha():
                    current_matching = p[p2]
                    if p2 + 1 < len(p) and p[p2 + 1] == "*":
                        p2 += 1
                        current_matching += p[p2]
                p2 += 1
                    
            matched = True
            if current_matching is not None:
                if current_matching == ".":
                    p1 += 1
                    current_matching = None
                elif current_matching.isalpha():
                    if s[p1] != current_matching:
                        matched = False
                    else:
                        p1 += 1
                        current_matching = None
            else:
                matched = False

            if (matched == False or p2 == len(p)) and pre_matching is not None:
                if pre_matching[-1] == "*":
                    if pre_matching[0] == ".":
                        p1 += 1
                        matched = True
                    elif pre_matching[0] == s[p1]:
                        p1 += 1
                        matched = True
            
            if not matched:
                return False                   
                
            pre_matching = current_matching
            
        return p1 == len(s) and p2 == len(p)
                      
        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    
    print(s.isMatch("a", ".*"))

