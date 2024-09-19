#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#
from typing import *
# @lc code=start
class Solution:
    def _canVisitAllRooms(self, rooms: list[list[int]], room_num: int, visited: list[bool]) -> bool:        
        can_visit = False
        room = rooms[room_num]
        visited[room_num] = True
        for key in room:
            if not visited[key]:
                can_visit = can_visit or self._canVisitAllRooms(rooms, key, visited)
        
        return can_visit
        
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in rooms]
        self._canVisitAllRooms(rooms, 0, visited)
        
        return all(visited)
        
# @lc code=end

