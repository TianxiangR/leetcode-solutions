#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#
from typing import *
# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            stack.append(ast)
            
            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
                if abs(stack[-1]) == abs(stack[-2]):
                    stack.pop()
                    stack.pop()
                elif abs(stack[-1]) > abs(stack[-2]):
                    last_one = stack.pop()
                    stack[-1] = last_one
                else:
                    stack.pop()
        
        return stack
        
# @lc code=end

