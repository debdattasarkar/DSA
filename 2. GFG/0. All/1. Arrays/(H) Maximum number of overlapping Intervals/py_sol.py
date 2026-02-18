class Solution:
    def overlapInt(self, arr):
        # Sweep line using events.
        # Inclusive intervals: if one ends at t and another starts at t -> they overlap.
        # So for same time, process START (+1) before END (-1).
        #
        # Time: O(n log n) due to sorting events
        # Space: O(n) for events list

        events = []

        for start, end in arr:
            events.append((start, +1))  # meeting starts -> add one active interval
            events.append((end, -1))    # meeting ends -> remove one (after counting at end time)

        # Sort by time; for tie: start(+1) should come before end(-1)
        # We can enforce this by sorting by (time, -delta) because +1 should be earlier than -1
        events.sort(key=lambda x: (x[0], -x[1]))

        active_intervals = 0
        max_overlap = 0

        for time, delta in events:
            active_intervals += delta
            max_overlap = max(max_overlap, active_intervals)

        return max_overlap