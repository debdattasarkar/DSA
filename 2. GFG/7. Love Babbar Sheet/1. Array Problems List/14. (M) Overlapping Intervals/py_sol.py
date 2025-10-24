class Solution:
	def mergeOverlap(self, arr):
		"""
        Merge overlapping (closed) intervals.
        - Overlap rule: [L1,R1] overlaps [L2,R2] iff L2 <= R1
        Time  : O(n log n) due to sort
        Space : O(1) extra (aside from output) if in-place sort is allowed
        """
        if not arr:
            return []

        # 1) Sort by start (then by end for determinism)
        arr.sort(key=lambda it: (it[0], it[1]))  # O(n log n)

        merged = []
        curL, curR = arr[0][0], arr[0][1]       # current merged interval

        # 2) Scan left → right, merging on the fly
        for i in range(1, len(arr)):
            L, R = arr[i]
            if L <= curR:                       # overlap → extend current
                curR = max(curR, R)
            else:                               # no overlap → flush current
                merged.append([curL, curR])
                curL, curR = L, R

        # 3) Push the final interval
        merged.append([curL, curR])
        return merged