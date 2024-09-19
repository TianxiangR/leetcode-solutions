#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
from typing import *
from collections import defaultdict
# @lc code=start
class Solution:
    def _findPath(self, _from: str, _to: str, graph: dict[str, dict[str, float]], visited: dict[str, bool], curr_value: float = 1.0) -> float:
        if _to in graph[_from]:
            return graph[_from][_to] * curr_value
        
        visited[_from] = True
        for _next in graph[_from].keys():
            if not visited[_next]:
                ret = self._findPath(_next, _to, graph, visited, curr_value * graph[_from][_next])
                if ret != -1.0:
                    return ret
        
        return -1.0
                
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph: dict[str, dict[str, float]] = defaultdict(defaultdict)
        
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1/value
            graph[a][a] = 1.0
            graph[b][b] = 1.0
        
        output = []
        for (a, b) in queries:
            if a in graph and b in graph:
                visited = {}
                for key in graph.keys():
                    visited[key] = False
                output.append(self._findPath(a, b, graph, visited))
            else:
                output.append(-1.0)
        
        return output
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values = [3.0,4.0,5.0,6.0]
    queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    
    solution.calcEquation(equations, values, queries)

