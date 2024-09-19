from typing import *
import math

class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        output, _, _ = 0, jobs.sort(), workers.sort()
        
        for i in reversed(range(len(jobs))):
          output = max(output, math.ceil(jobs[i] / workers[i]))
        
        return output