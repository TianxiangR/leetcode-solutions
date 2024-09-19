#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from typing import *

# @lc code=start

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(numCourses)]
        
        for main, pre in prerequisites:
            courses[main].append(pre)
        
        memo = [False] * numCourses
        inStack = [False] * numCourses
        
        def _canFinish(num: int) -> bool:
            if inStack[num]:
                memo[num] = False
                return False
            if memo[num]:
                return memo[num]
            inStack[num] = True
            pres = courses[num]
            
            for pre in pres:
                if not _canFinish(pre):
                    return False
            
            inStack[num] = False
            memo[num] = True    
            return True
        
        for i in range(numCourses):
            if not _canFinish(i):
                return False
        
        return True
            
        
            
            
        
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    solution.canFinish(2, [[1, 0]])

