class Solution:
    def maxSum(self, arr): 
        """
        Maximize sum(i * arr[i]) over all rotations.

        Approach:
          - Precompute S = sum(arr) and R0 = sum(i * arr[i]).
          - For k = 1..n-1 (clockwise rotations), use:
                R_next = R_curr + S - n * arr[n - k]
            Track the maximum across all R_k.

        Time:  O(n)
        Space: O(1)
        """
        n = len(arr)
        if n <= 1:
            return 0 if n == 0 else 0  # only i=0 term

        S = sum(arr)                           # O(n)
        R0 = sum(i * arr[i] for i in range(n)) # O(n)

        best = R0
        curr = R0
        # After k clockwise rotations, the element moved to front is arr[n - k]
        for k in range(1, n):                  # O(n)
            curr = curr + S - n * arr[n - k]
            if curr > best:
                best = curr
        return best