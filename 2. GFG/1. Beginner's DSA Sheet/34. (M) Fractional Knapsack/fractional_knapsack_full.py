#!/usr/bin/env python3
"""
Fractional Knapsack — Full Program (with inline time/space complexity notes)
----------------------------------------------------------------------------
- Implements three variants: optimized sort, heap, and a simple brutish scan.
- Demonstrates on sample inputs and reports the total runtime of the program.
"""

from typing import List, Tuple
import timeit
import random

class Solution:
    def fractionalKnapsack(self, val: List[int], wt: List[int], capacity: int) -> float:
        """
        Optimized Greedy (sort by value/weight ratio).

        Steps and complexities:
        1) Build (ratio, value, weight) list:
           - Time:  O(n) to compute n ratios
           - Space: O(n) to store the tuples
        2) Sort by ratio descending:
           - Time:  O(n log n) (dominant)
           - Space: O(n) auxiliary in Python's Timsort (worst-case)
        3) Single pass to fill knapsack:
           - Time:  O(n)
           - Space: O(1) extra
        Overall: Time O(n log n), Space O(n)
        """
        n = len(val)
        # Build list of (ratio, value, weight)  ---- O(n) time, O(n) space
        items: List[Tuple[float, int, int]] = [(val[i]/wt[i], val[i], wt[i]) for i in range(n)]

        # Sort by ratio descending  ---- O(n log n) time, O(n) space
        items.sort(key=lambda x: x[0], reverse=True)

        total_value = 0.0
        remaining = capacity

        # Greedy pick  ---- O(n) time, O(1) space
        for ratio, v, w in items:
            if remaining == 0:
                break
            if w <= remaining:
                total_value += v
                remaining -= w
            else:
                # Take the fraction that fits and stop
                fraction = remaining / w
                total_value += v * fraction
                remaining = 0
                break

        # Round to 6 decimals as required
        return round(total_value, 6)

    def fractionalKnapsack_heap(self, val: List[int], wt: List[int], capacity: int) -> float:
        """
        Heap-based Greedy (priority queue keyed by ratio).

        Build a max-heap of ratios:
          - Python uses a min-heap, so push negative ratios.
        Complexities:
          - Building heap: O(n)
          - Each pop: O(log n), up to n pops => O(n log n) time overall
          - Space: O(n) for the heap
        """
        import heapq
        heap = [(-(v/w), v, w) for v, w in zip(val, wt)]  # O(n) build list
        heapq.heapify(heap)  # O(n)

        total = 0.0
        remaining = capacity
        while remaining > 0 and heap:
            _, v, w = heapq.heappop(heap)  # O(log n)
            if w <= remaining:
                total += v
                remaining -= w
            else:
                total += v * (remaining / w)
                remaining = 0
                break

        return round(total, 6)

    def fractionalKnapsack_brutish(self, val: List[int], wt: List[int], capacity: int) -> float:
        """
        Simple 'brutish' approach for clarity (not for large n):

        Repeatedly scan all remaining items to find the best ratio.
        Complexities:
          - Each selection scans O(n)
          - Up to n selections in worst case
          - Time: O(n^2) worst-case
          - Space: O(n) for the 'used' flags
        """
        n = len(val)
        used = [False] * n
        total = 0.0
        remaining = capacity

        while remaining > 0:
            best_ratio, idx = -1.0, -1
            for i in range(n):  # O(n) scan
                if not used[i]:
                    r = val[i] / wt[i]
                    if r > best_ratio:
                        best_ratio, idx = r, i

            if idx == -1:  # nothing left
                break

            used[idx] = True
            if wt[idx] <= remaining:
                total += val[idx]
                remaining -= wt[idx]
            else:
                total += val[idx] * (remaining / wt[idx])
                remaining = 0
                break

        return round(total, 6)


def main():
    print("==== Fractional Knapsack — Full Program Demo ====")

    sol = Solution()

    # ---------- Input Set 1 (from prompt) ----------
    val1, wt1, cap1 = [60, 100, 120], [10, 20, 30], 50
    print("\\nInput 1:")
    print("  val =", val1)
    print("  wt  =", wt1)
    print("  capacity =", cap1)
    ans1 = sol.fractionalKnapsack(val1, wt1, cap1)
    print("  Output (optimized):", f"{ans1:.6f}")  # expected 240.000000

    # ---------- Input Set 2 (from prompt) ----------
    val2, wt2, cap2 = [500], [30], 10
    print("\\nInput 2:")
    print("  val =", val2)
    print("  wt  =", wt2)
    print("  capacity =", cap2)
    ans2 = sol.fractionalKnapsack(val2, wt2, cap2)
    print("  Output (optimized):", f"{ans2:.6f}")  # expected ≈166.666667

    # ---------- Show alternative implementations on Input 1 ----------
    print("\\nAlternative implementations on Input 1:")
    print("  Heap version:    ", f"{sol.fractionalKnapsack_heap(val1, wt1, cap1):.6f}")
    print("  Brutish version: ", f"{sol.fractionalKnapsack_brutish(val1, wt1, cap1):.6f}")

    # ---------- Optional: one random test for scale ----------
    random.seed(42)
    n = 2000
    valR = [random.randint(1, 1000) for _ in range(n)]
    wtR  = [random.randint(1, 1000) for _ in range(n)]
    capR = sum(wtR) // 3
    print("\\nRandom test size n =", n, " capacity ~", capR)

    # Timing the optimized approach on the random test once (not part of 'full program time')
    t0 = timeit.default_timer()
    ansR = sol.fractionalKnapsack(valR, wtR, capR)
    t1 = timeit.default_timer()
    print("  Optimized value =", f"{ansR:.6f}")
    print("  Optimized run time =", f"{(t1 - t0):.6f}", "seconds")

if __name__ == "__main__":
    # Measure the full program runtime of 'main' using timeit-like timer.
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")
