class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        """
        One-pass insertion using the sorted, non-overlapping property.

        Time:  O(n) - each interval visited once
        Space: O(n) - for the output list
        """
        res = []
        i = 0
        n = len(intervals)
        ns, ne = newInterval  # newStart, newEnd

        # 1) Add all intervals strictly to the left of newInterval
        #    (end < newStart)
        while i < n and intervals[i][1] < ns:
            res.append(intervals[i])
            i += 1

        # 2) Merge all intervals that overlap with [ns, ne]
        #    Overlap if intervals[i].start <= ne
        while i < n and intervals[i][0] <= ne:
            ns = min(ns, intervals[i][0])
            ne = max(ne, intervals[i][1])
            i += 1
        res.append([ns, ne])  # push the merged block

        # 3) Append remaining intervals (to the right of merged new)
        while i < n:
            res.append(intervals[i])
            i += 1

        return res