class Solution:
    def getMinDiff(self, arr, k):
        """
        Greedy after sorting.
        Time:  O(n log n) for sort + O(n) scan
        Space: O(1) extra (in-place or O(n) if a copy is made)
        """
        n = len(arr)
        if n <= 1:
            return 0

        arr.sort()  # O(n log n)

        # Initial spread with no changes
        ans = arr[-1] - arr[0]

        # Candidate extremes if we raise the left and lower the right
        base_small = arr[0] + k
        base_big   = arr[-1] - k

        # Ensure small <= big to make min/max reasoning simple
        if base_small > base_big:
            base_small, base_big = base_big, base_small

        # Try every split i (left side +k, right side -k)
        for i in range(1, n):
            # If decreasing this makes it negative, it violates the constraint
            if arr[i] - k < 0:
                continue

            # Smallest could be either the raised smallest or the decreased current
            small = min(base_small, arr[i] - k)

            # Largest could be either the increased previous or the lowered largest
            big   = max(base_big,   arr[i-1] + k)

            ans = min(ans, big - small)

        return ans