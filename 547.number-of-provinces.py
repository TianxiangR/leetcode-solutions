#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#
from typing import *
# @lc code=start
class Solution:
    def _findCircleNum(self, isConnected: list[list[int]], visited: list[bool], city: int) -> int:
        if visited[city]:
            return 0
        
        connectivities = isConnected[city]
        
        visited[city] = True
        for i in range(len(connectivities)):
            city_num = i
            connected = bool(connectivities[i])
            if not visited[city_num] and connected:
                self._findCircleNum(isConnected, visited, city_num)
        
        return 1
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        output = 0
        visited = [False for _ in isConnected]
        for i in range(len(isConnected)):
            output += self._findCircleNum(isConnected, visited, i)
        
        return output
        
        
# @lc code=end

