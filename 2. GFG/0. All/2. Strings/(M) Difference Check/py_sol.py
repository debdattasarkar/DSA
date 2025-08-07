class Solution:
    def minDifference(self, arr):
        # Helper to convert "HH:MM:SS" to seconds
        def to_seconds(t):
            h, m, s = map(int, t.split(":"))
            return h * 3600 + m * 60 + s

        # Convert all times to seconds
        times = [to_seconds(t) for t in arr]

        # Sort times
        times.sort()

        # Initialize min_diff as max possible (1 day in seconds)
        min_diff = float('inf')
        n = len(times)

        # Compare adjacent times
        for i in range(1, n):
            diff = times[i] - times[i - 1]
            min_diff = min(min_diff, diff)

        # Also check circular diff between last and first
        wrap_around = 86400 + times[0] - times[-1]  # 86400 = 24*60*60
        min_diff = min(min_diff, wrap_around)

        return min_diff