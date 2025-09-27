class Solution:
    def sumExceptFirstLast(self,arr):
        # Parr:  list of pair
        n = len(arr)                      # O(1)
        if n <= 2:                        # O(1) — edge case
            return 0
        # Use built-in sum once; Python sums in O(n).
        # Extra space: O(1).
        return sum(arr) - arr[0] - arr[-1]