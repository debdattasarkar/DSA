class Solution:
    def minMen(self, arr):
        #code here 
        n = len(arr)
        if n == 0:
            return 0

        # Build coverage intervals for all available workers
        # Time: O(n), Space: O(n)
        intervals = []
        for i, radius in enumerate(arr):
            if radius == -1:
                continue
            left = max(0, i - radius)
            right = min(n - 1, i + radius)
            intervals.append((left, right))

        # If no intervals, can't cover anything
        if not intervals:
            return -1

        # Sort by start time
        # Time: O(n log n)
        intervals.sort()

        workers_used = 0
        idx = 0
        current_hour = 0  # we need to cover from this hour onward

        while current_hour <= n - 1:
            farthest_reach = -1

            # Among all intervals that start at/before current_hour,
            # pick the one that reaches farthest right.
            # Total scanning across the loop is O(n)
            while idx < len(intervals) and intervals[idx][0] <= current_hour:
                farthest_reach = max(farthest_reach, intervals[idx][1])
                idx += 1

            # If we can't extend coverage, impossible
            if farthest_reach < current_hour:
                return -1

            # We choose one worker (the best reach found)
            workers_used += 1

            # Next uncovered hour is farthest_reach + 1
            current_hour = farthest_reach + 1

        return workers_used