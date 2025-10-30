#User function Template for python3

class Solution:
    def getMinDiff(self,arr,k):
        """
        Greedy (expected in interviews):
          1) Sort.
          2) Start with baseline answer (max - min).
          3) For each split i (1..n-1):
                left side gets +k, right side gets -k
             Compute min & max formed by borders and update best.
        Time  : O(n log n) for sort + O(n) scan
        Space : O(1) extra (in-place)
        """
        n = len(arr)
        if n <= 1:
            return 0
        arr.sort()  # O(n log n)

        # Baseline with no modifications
        best_diff = arr[-1] - arr[0]

        # If k == 0, nothing changes
        if k == 0:
            return best_diff

        # Scan all cut positions
        smallest_after_raise = arr[0] + k       # candidate when left side is raised
        largest_after_lower  = arr[-1] - k      # candidate when right side is lowered

        for i in range(1, n):
            # Left segment [0..i-1] uses +k, Right segment [i..n-1] uses -k
            min_height = min(smallest_after_raise, arr[i] - k)
            max_height = max(arr[i-1] + k,       largest_after_lower)
            best_diff = min(best_diff, max_height - min_height)

        return best_diff