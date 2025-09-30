#User function Template for python3

class Solution:
    def minAmount(self, A, n): 
        # Edge case: no tasks
        if n == 0:
            return 0
        
        # Initialize for i = 0
        # do  : minimum time if we DO task 0  -> pay A[0]
        # skip: minimum time if we SKIP task 0 -> 0 (skipping a single task is allowed)
        do = A[0]
        skip = 0
        
        # Iterate tasks 1..n-1; each step is O(1), total O(N)
        for i in range(1, n):
            # If we do task i, previous can be do or skip; take the cheaper
            new_do = min(do, skip) + A[i]
            # If we skip task i, previous MUST have been done (can't skip twice)
            new_skip = do
            
            do, skip = new_do, new_skip
        
        # Final answer: can end by doing or skipping the last task
        # Space used is O(1) (only a few scalars).
        return min(do, skip)
