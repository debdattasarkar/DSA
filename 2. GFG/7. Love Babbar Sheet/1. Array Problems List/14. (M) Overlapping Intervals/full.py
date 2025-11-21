#!/usr/bin/env python3
"""
Overlapping Intervals — Merge all overlapping closed intervals.
Strategy: sort by start, sweep once, extend current interval or flush to output.

Complexities:
- Sorting: O(n log n) time, O(1) extra if in-place (Python's Timsort uses O(n) aux on worst cases; we ignore that here).
- Single pass merge: O(n) time.
- Output: O(k) intervals (k <= n).
Overall: O(n log n) time, O(1) extra beyond output.
"""

from time import perf_counter
import timeit
from typing import List


class Solution:
    def mergeOverlap(self, arr: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals (closed intervals).
        Overlap rule: [a,b] overlaps [c,d] iff c <= b.

        Parameters
        ----------
        arr : List[List[int]]
            List of [start, end], may be unsorted.

        Returns
        -------
        List[List[int]] : merged, non-overlapping intervals sorted by start.
        """
        # Edge case: empty input → O(1)
        if not arr:
            return []

        # 1) SORT by start (then end for determinism)
        #    Time: O(n log n). Space: O(1) extra (conceptually).
        arr.sort(key=lambda it: (it[0], it[1]))

        # 2) SWEEP once left→right; keep current merged interval
        #    Time: O(n). Space: O(1) beyond result.
        merged: List[List[int]] = []
        curL, curR = arr[0]

        for i in range(1, len(arr)):
            L, R = arr[i]
            if L <= curR:                 # Overlap → extend
                # O(1) update
                if R > curR:
                    curR = R
            else:
                # No overlap → flush current interval
                merged.append([curL, curR])  # Amortized O(1)
                curL, curR = L, R            # Start new

        # 3) Push the tail interval — O(1)
        merged.append([curL, curR])
        return merged


# -------------------------- Demonstration & Timing --------------------------

def demo():
    cases = [
        # From prompt style
        ([[1,3], [2,4], [6,8], [9,10]],
         [[1,4], [6,8], [9,10]]),

        ([[6,8], [1,9], [2,4], [4,7]],
         [[1,9]]),

        # More edge-ish cases
        ([], []),
        ([[1,5]], [[1,5]]),
        ([[1,2], [3,4]], [[1,2], [3,4]]),             # disjoint
        ([[1,10], [2,3], [4,5], [6,7], [8,9]], [[1,10]]),  # nested
        ([[1,2], [2,3], [3,4]], [[1,4]]),             # touching (closed intervals → merge)
    ]

    sol = Solution()
    print("=== Sample I/O ===")
    for arr, expected in cases:
        start = perf_counter()
        out = sol.mergeOverlap([x[:] for x in arr])  # copy for safety
        dur = (perf_counter() - start) * 1e6
        print(f"Input : {arr}")
        print(f"Output: {out}   (took {dur:.1f} µs)")
        if expected is not None:
            print(f"Expect: {expected}")
        print("-" * 50)

    # Timing on a larger random case
    import random
    random.seed(7)
    n = 200_000
    # Create random intervals with start<=end
    big = []
    for _ in range(n):
        a = random.randint(0, 1_000_000)
        b = a + random.randint(0, 1000)
        big.append([a, b])

    sol = Solution()
    avg = timeit.timeit("sol.mergeOverlap(big[:])", number=3, globals={"sol": sol, "big": big}) / 3
    print(f"\nAverage time on n={n} intervals over 3 runs: {avg:.3f} s")

    print("\nComplexity recap:")
    print("  Sort  : O(n log n)")
    print("  Sweep : O(n)")
    print("  Extra : O(1) beyond the output list")


if __name__ == "__main__":
    demo()