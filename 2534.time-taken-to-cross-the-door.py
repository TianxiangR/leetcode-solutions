from typing import *
from collections import deque
class Solution:
    def timeTaken(self, arrivals: List[int], states: List[int]) -> List[int]:
        output = [0 for _ in range(len(arrivals))]
            
        enter_q: deque[tuple[int, int]] = deque()
        exit_q: deque[tuple[int, int]] = deque()
        
        curr_time = 0
        last_direction = 1
        for i in range(len(arrivals)):
          if arrivals[i] - curr_time > 0:
            last_direction = 1
          
          curr_time = arrivals[i]
          
          if states[i] == 0:
            enter_q.append(i)
          else:
            exit_q.append(i)
            
          while (i + 1 == len(arrivals) or curr_time < arrivals[i + 1]) and (len(enter_q) or len(exit_q)):
            if last_direction == 1 and len(exit_q):
              output[exit_q.popleft()] = curr_time
            elif enter_q:
              output[enter_q.popleft()] = curr_time
              last_direction = 0
            else:
              output[exit_q.popleft()] = curr_time
              last_direction = 1
            
            
            curr_time += 1

            
        return output
          
              