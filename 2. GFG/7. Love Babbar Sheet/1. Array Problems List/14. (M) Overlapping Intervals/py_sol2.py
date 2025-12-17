class Solution:
	def mergeOverlap(self, arr):
		"""
        Merge overlapping intervals.

        Parameters:
            arr: List of intervals [start, end].

        Returns:
            A new list of non-overlapping intervals sorted by start,
            where any overlapping intervals have been merged.

        Overall Complexity:
            Let n = len(arr).

            - Sorting intervals: O(n log n)
            - Single pass to merge: O(n)
            => Time  : O(n log n)
            - Extra space (besides result): O(1) if we sort arr in-place,
                                            O(n) for the output list itself.
        """
        n = len(arr)
        if n == 0:
            return []

        # 1) Sort intervals by their start time.
        #    Time: O(n log n), Space: O(1) extra (in-place sort).
        arr.sort(key=lambda interval: interval[0])

        merged: List[List[int]] = []

        # 2) Initialize the current interval to the first one.
        current_start, current_end = arr[0]

        # 3) Iterate over the remaining intervals and merge overlapping ones.
        #    Single pass: O(n).
        for i in range(1, n):
            next_start, next_end = arr[i]

            if next_start <= current_end:
                # Overlap: extend the current interval's end if needed.
                # O(1) operation.
                current_end = max(current_end, next_end)
            else:
                # No overlap: push the finished current interval to result,
                # and start a new current interval.
                merged.append([current_start, current_end])
                current_start, current_end = next_start, next_end

        # 4) Append the last remaining current interval.
        merged.append([current_start, current_end])

        return merged