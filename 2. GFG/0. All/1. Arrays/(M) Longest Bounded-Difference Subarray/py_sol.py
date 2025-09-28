import heapq

class Solution:
    def longestSubarray(self, arr, x):
        """
        Maintain min-heap and max-heap (as negatives) of (value, index).
        Use lazy deletion: when top index < L, pop and continue.
        Expand R; while max - min > x, increment L.
        Time:  O(n log n)
        Space: O(n)
        """
        n = len(arr)
        if n == 0:
            return []

        minH = []  # (val, idx)
        maxH = []  # (-val, idx)
        L = 0
        bestL, bestLen = 0, 0

        for R, v in enumerate(arr):
            heapq.heappush(minH, (v, R))
            heapq.heappush(maxH, (-v, R))

            # Clean tops to respect current L
            def top_min():
                while minH and minH[0][1] < L:
                    heapq.heappop(minH)
                return minH[0][0] if minH else None

            def top_max():
                while maxH and maxH[0][1] < L:
                    heapq.heappop(maxH)
                return -maxH[0][0] if maxH else None

            # Shrink while invalid
            while top_max() - top_min() > x:
                L += 1  # lazy deletion: indices < L will be popped on next access

            curLen = R - L + 1
            if curLen > bestLen or (curLen == bestLen and L < bestL):
                bestLen, bestL = curLen, L

        return arr[bestL:bestL + bestLen]