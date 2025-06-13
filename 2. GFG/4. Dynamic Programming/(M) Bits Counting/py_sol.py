from typing import List

class Solution:
    def countBits(self, n : int) -> List[int]:
        # code here
        # Initialize result list with zeros
        res = [0] * (n + 1)
        
        # Start from 1 to n
        for i in range(1, n + 1):
            # Use the relation: res[i] = res[i >> 1] + (i & 1)
            res[i] = res[i >> 1] + (i & 1)
        
        return res
        