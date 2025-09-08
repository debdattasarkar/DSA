class Solution:
    def assignHole(self, mices, holes):
        """
        Greedy optimal (1D bottleneck assignment):
          1) Sort both arrays.
          2) Pair i-th mouse to i-th hole.
          3) Answer = max |mices[i] - holes[i]|.

        Time:  O(n log n)  (sorting dominates)
        Space: O(1) extra (if sorting in-place) or O(n) depending on sort impl.
        """
        n = len(mices)
        if n != len(holes):
            # Problem statement guarantees equal sizes; guard anyway
            raise ValueError("mices and holes must have the same length")

        mices.sort()
        holes.sort()

        worst = 0
        for i in range(n):                       # O(n)
            worst = max(worst, abs(mices[i] - holes[i]))
        return worst