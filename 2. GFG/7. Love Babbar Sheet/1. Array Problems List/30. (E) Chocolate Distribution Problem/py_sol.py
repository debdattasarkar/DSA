#User function Template for python3
class Solution:
    def findMinDiff(self, arr,M):
        """
        Optimized: sort + sliding window
        Time:  O(n log n) for sorting + O(n) scan
        Space: O(1) auxiliary (sort in-place; ignore recursion)
        Returns the minimum possible difference (max-min) among any M packets;
        -1 if M > n. For M in {0,1}, result is 0.
        """
        n = len(arr)
        if M == 0 or M == 1:
            return 0
        if M > n:
            return -1

        # sort packets by chocolates — O(n log n)
        arr.sort()

        # slide a window of size M, track minimal spread — O(n)
        best = float('inf')
        for i in range(n - M + 1):
            spread = arr[i + M - 1] - arr[i]  # max - min in this window
            if spread < best:
                best = spread

        return best