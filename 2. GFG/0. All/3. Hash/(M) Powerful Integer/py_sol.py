from collections import defaultdict
class Solution:
    def powerfulInteger(self, intervals, k):
        # Step 1: Build the event map (like prefix difference array)
        events = defaultdict(int)

        for start, end in intervals:
            events[start] += 1
            events[end + 1] -= 1

        # Step 2: Sort event points
        sorted_points = sorted(events.keys())

        count = 0
        ans = -1

        # We will scan through all the event points and track "active range"
        for i in range(len(sorted_points) - 1):
            point = sorted_points[i]
            count += events[point]

            next_point = sorted_points[i + 1]

            # If count >= k, all numbers in range [point, next_point - 1] are valid
            if count >= k:
                ans = max(ans, next_point - 1)

        return ans
