#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#
from typing import *
# @lc code=start
class Solution:
    def _minReorder(self, edges: dict[int, int], reversedEdges: dict[int, int], visited: list[bool], node_num: int) -> int:
        if visited[node_num]:
            return 0
        
        output = 0
        outs = edges.get(node_num, [])
        visited[node_num] = True
        for _to in outs:
            if not visited[_to]:
                output += self._minReorder(edges, reversedEdges, visited, _to) + 1
        
        ins = reversedEdges.get(node_num, [])
        for _from in ins:
            if not visited[_from]:
                output += self._minReorder(edges, reversedEdges, visited, _from)
        
        return output
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges: dict[int, list[int]] = {}
        reversedEdges: dict[int, list[int]] = {}
        visited = [False for _ in range(n)]
        
        for _from, _to in connections:
            if _from in edges:
                edges[_from].append(_to)
            else:
                edges[_from] = [_to]
            if _to in reversedEdges:
                reversedEdges[_to].append(_from)
            else:
                reversedEdges[_to] = [_from]
        
        return self._minReorder(edges, reversedEdges, visited, 0)
        
        
        
        
        
# @lc code=end

