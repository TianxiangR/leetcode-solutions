from typing import *

def memoize(func):
    cache = {}
    def memoized_func(*args):
        if args in cache:
            return cache[args]  # Return the cached result
        result = func(*args)  # Call the function if not in cache
        cache[args] = result  # Store the result in cache
        return result
    return memoized_func

@memoize
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def combination(n: int, r: int) -> int:
  return factorial(n) // (factorial(r) * factorial(n - r))

class Solution:
    def _sumN(self, n: int) -> int:
        return n * (n + 1) // 2
  
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        num_set: dict[int, bool] = dict()
        
        for num in nums:
          num_set[num] = True
        
        arith_seqs = []
        
        while len(num_set):
          first_key = next(iter(num_set))
          seq = [first_key]
          curr_num = first_key
          while curr_num + k in num_set:
            seq.append(curr_num + k)
            del num_set[curr_num + k]
          
          arith_seqs.append(seq)
        
        ans = 0
        for seq in arith_seqs:
        
        
        
        