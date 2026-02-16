class Solution:
    def canAttend(self, arr):
        # Sort by start time, then check adjacent meetings
        # Time: O(n log n), Space: O(1) auxiliary (ignoring sort internals)
        arr.sort(key=lambda interval: interval[0])

        # Track the end time of the last meeting we attended
        previous_end_time = arr[0][1]

        for i in range(1, len(arr)):
            current_start_time, current_end_time = arr[i]

            # Overlap condition
            if current_start_time < previous_end_time:
                return False

            # Update the end time boundary
            previous_end_time = current_end_time

        return True
