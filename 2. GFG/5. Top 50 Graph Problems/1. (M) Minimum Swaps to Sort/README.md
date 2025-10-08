# Minimum Swaps to Sort

**Difficulty:** Medium
**Accuracy:** 38.39%
**Submissions:** 182K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given an array **arr[]** of distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.

---

## Examples

### Example 1

**Input:** `arr[] = [2, 8, 5, 4]`
**Output:** `1`
**Explanation:** Swap 8 with 4 to get the sorted array.

---

### Example 2

**Input:** `arr[] = [10, 19, 6, 3, 5]`
**Output:** `2`
**Explanation:** Swap 10 with 3 and 19 with 5 to get the sorted array.

---

### Example 3

**Input:** `arr[] = [1, 3, 4, 5, 6]`
**Output:** `0`
**Explanation:** Input array is already sorted.

---

## Constraints

* (1 \le \text{arr.size()} \le 10^5)
* (1 \le \text{arr}[i] \le 10^9)

---

## Expected Complexities

* **Time Complexity:** (O(n \log n))
* **Auxiliary Space:** (O(n))

---

## Company Tags

* Microsoft

---

## Topic Tags

* Arrays
* Sorting
* Graph
* Data Structures
* Algorithms

---

## Related Articles

* Cycle Sort
* Minimum Number Swaps Required Sort Array

---

---

gotcha — here’s an interview-ready pack: clear explanation, step-by-step dry run, and multiple Python solutions in your requested template.

---

# 2) Intuition + Step-by-Step Dry Run

## Core idea (what’s being minimized?)

You may swap **any two** positions. If you write where each element must go in the **sorted array**, the permutation splits into **cycles**.

* A cycle of length `L` needs exactly `L − 1` swaps to put all its members in correct places (swap one “pivot” with each of the remaining `L−1` items).
* Therefore, **minimum swaps = Σ (cycle_length − 1) over all cycles**.

This is the standard and optimal solution.

---

## Dry run 1 — `arr = [2, 8, 5, 4]`

1. Pair each value with its original index and sort by value:
   `with_idx = [(2,0), (4,3), (5,2), (8,1)]`
   This tells us the **target index** for each original index.

2. Build the index mapping:

* At original index 0 (`2`), target index is 0 → already correct → 1-cycle contributes 0 swaps.
* At original index 1 (`8`), target index is 3.
* At original index 3 (`4`), target index is 1.
  They form cycle `1 → 3 → 1` of length 2 → contributes `2−1 = 1`.
* At original index 2 (`5`), target index is 2 → 1-cycle contributes 0.

3. Sum: `1` → **answer = 1**.

(Concretely: swap `8` and `4` → array becomes `[2, 4, 5, 8]`.)

---

## Dry run 2 — `arr = [10, 19, 6, 3, 5]`

1. Pair + sort:
   Original indices with sorted order by value
   `[(3,3), (5,4), (6,2), (10,0), (19,1)]`
   i.e., value 3 from idx 3 goes to new idx 0; value 5 from idx 4 → new idx 1; … value 19 from idx 1 → new idx 4.

2. Follow cycles over **original indices** → **target indices**:

* Start at index 0 (value 10). Its sorted target is index 3 (because 10 is the 4th smallest).
  Index 3 (value 3) targets index 0 → cycle `(0 → 3 → 0)` length 2 → contributes 1 swap.
* Next unvisited index 1 (value 19). Its target is 4.
  Index 4 (value 5) targets 1 → cycle `(1 → 4 → 1)` length 2 → contributes 1 swap.
* Index 2 (value 6) targets 2 → 1-cycle contributes 0.

Total swaps: `1 + 1 = 2`.
(Concretely: swap `10↔3`, then `19↔5`.)

---

# 3) Python solutions (multiple ways, interview-ready)

### A) Cycle decomposition (canonical optimal)

```python
class Solution:
    
    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, arr):
        """
        Idea: sort value-index pairs to know each element's target position.
        Walk permutation cycles; sum (cycle_len - 1).

        Time:  O(n log n) for the sort, O(n) to walk cycles
        Space: O(n) for pairs + visited
        """
        n = len(arr)
        # Pair each value with its original index, then sort by value
        with_idx = [(val, i) for i, val in enumerate(arr)]      # O(n)
        with_idx.sort(key=lambda x: x[0])                        # O(n log n)

        visited = [False] * n                                    # O(n) space
        swaps = 0

        for i in range(n):                                       # O(n)
            # If already visited or already in correct place, skip
            if visited[i] or with_idx[i][1] == i:
                continue

            # Follow the cycle starting at i
            cycle_len = 0
            j = i
            while not visited[j]:                                # each index visited once overall
                visited[j] = True
                # Jump to the index where the current element originally came from
                j = with_idx[j][1]
                cycle_len += 1

            if cycle_len > 0:
                swaps += cycle_len - 1                           # L-1 swaps per cycle

        return swaps
```

---

### B) “Place-correct” greedy (equivalent to cycles, easy to reason)

* Build a map `val → sorted_index`.
* Scan `i` from left to right; if `arr[i]` is not the value that should be at `i`, swap it with the element that *should* be here.
* Update the map in O(1) and continue.
* This performs exactly one swap per element that is “out of cycle pivot”, so the total equals the cycle formula.

```python
class Solution:
    
    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, arr):
        """
        Greedy: put each position's correct value in place via one swap.
        Maintain a value->current_index map to do O(1) lookups.

        Time:  O(n log n) to precompute the sorted order + O(n) swaps
        Space: O(n) for the maps
        """
        n = len(arr)
        # Sorted target order
        sorted_vals = sorted(arr)                                 # O(n log n)

        # Map each value to its current index in 'arr'
        pos = {v: i for i, v in enumerate(arr)}                   # O(n)
        swaps = 0

        for i in range(n):                                        # O(n)
            correct_val = sorted_vals[i]
            if arr[i] == correct_val:
                continue  # already good

            # Index where the correct_val currently resides
            j = pos[correct_val]

            # Swap arr[i] <-> arr[j]
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1

            # Update indices in the map after swap
            pos[arr[j]] = j
            pos[arr[i]] = i

        return swaps
```

> Note: This mutates `arr`. If mutation is undesirable, work on a copy.

---

### C) Baseline “selection-sort style count” (simple, shows the same principle)

This is essentially (B) written to look like selection sort: at each `i`, the value that should be at `i` is `sorted_vals[i]`; if it isn’t already there, you swap once with its current location. It’s still optimal and runs in the same complexity.

```python
class Solution:
    
    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, arr):
        """
        Selection-style: for each i, ensure the i-th smallest is at i, swapping once if needed.

        Time:  O(n log n) for sorting + O(n) passes
        Space: O(n) due to value->index map
        """
        n = len(arr)
        sorted_vals = sorted(arr)                                 # O(n log n)
        index_of = {v: i for i, v in enumerate(arr)}              # O(n)
        swaps = 0

        for i in range(n):                                        # O(n)
            want = sorted_vals[i]
            if arr[i] == want:
                continue
            j = index_of[want]   # where the desired value currently is

            # swap into place
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1

            # map updates
            index_of[arr[j]] = j
            index_of[arr[i]] = i

        return swaps
```

All three approaches return the **minimum** number of swaps.

---

# 4) Likely Interview Q&A

**Q1. Why does the cycle formula give the minimum?**
**A.** Any permutation decomposes into disjoint cycles. To fix a cycle of length `L`, at least `L−1` swaps are necessary (each swap can place at most one new element in its final position, and one element must serve as the pivot). Conversely, `L−1` swaps suffice by holding one index fixed and swapping it with each incorrectly placed element in the cycle. Summing over cycles is thus optimal.

**Q2. What’s the time and space complexity?**
**A.** Sorting dominates: **O(n log n)** time and **O(n)** space (for the pairs/visited or maps). The cycle walk is O(n).

**Q3. Can we do better than O(n log n)?**
**A.** With arbitrary distinct values, you need the **relative order** (i.e., the sorted positions), which requires sorting. If the values are from `1..n` (i.e., a permutation), you can do it in **O(n)** by comparing to index (no sort).

**Q4. Is counting inversions the same as minimum swaps?**
**A.** No. Inversions count the minimum number of **adjacent** swaps (bubble-sort metric). We’re allowed to swap **any two** positions; that’s a different (smaller) number given by the cycle formula.

**Q5. Does your greedy swapping always yield the minimum?**
**A.** Yes—each swap places at least one element into its final position and mirrors the cycle-decomposition argument. The total swaps equal Σ(L−1) over cycles.

**Q6. How do you avoid revisiting elements in the cycle method?**
**A.** Maintain a `visited` array and skip indices that are already visited or already in correct position.

**Q7. What happens if elements are not distinct?**
**A.** The problem statement assumes distinct elements. With duplicates, mapping to unique targets isn’t well-defined—one must break ties (e.g., by original index) and the method becomes more nuanced.

**Q8. How would you prove correctness succinctly?**
**A.** (1) Any final sorted array corresponds to a permutation from original indices to sorted indices. (2) A permutation decomposes into cycles. (3) Each cycle requires at least `L−1` swaps and can be fixed with exactly `L−1`. Hence the sum is minimal and achievable.

---

---

awesome — here’s a **runnable, interview-style full program** for *Minimum Swaps to Sort*, with step-by-step complexity notes in code, a small driver that prints **inputs & outputs**, and **timeit** benchmarks. I’ve also added a short list of real-world uses at the end.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Minimum Swaps to Sort (distinct elements)

Approach used in Solution.minSwaps:
- Cycle decomposition of the permutation from current indices -> sorted indices.
- Each cycle of length L needs exactly (L - 1) swaps.

Complexities (high level):
- Time:  O(n log n)  # sorting dominates
- Space: O(n)        # pairs and visited (or maps in the greedy variant)
"""

import timeit
from typing import List


class Solution:
    # -------------------------------------------------------------
    # Function to find the minimum number of swaps required to sort the array.
    # -------------------------------------------------------------
    def minSwaps(self, arr: List[int]) -> int:
        """
        Cycle decomposition method (canonical optimal).
        Steps:
          1) Pair each value with its original index -> O(n)
          2) Sort pairs by value to know each element's target index -> O(n log n)
          3) Walk permutation cycles and sum (cycle_len - 1) -> O(n)

        Overall:
          Time:  O(n log n)
          Space: O(n)
        """
        n = len(arr)

        # (1) Pair values with their original indices  --- Time: O(n), Space: O(n)
        with_idx = [(val, i) for i, val in enumerate(arr)]

        # (2) Sort by value to get target order         --- Time: O(n log n)
        with_idx.sort(key=lambda x: x[0])

        # visited flags for cycle detection             --- Space: O(n)
        visited = [False] * n

        swaps = 0

        # (3) Walk each cycle exactly once              --- Time: O(n)
        for i in range(n):
            # Already in correct position OR already processed in a cycle
            if visited[i] or with_idx[i][1] == i:
                # Checking/branching itself is O(1)
                continue

            # Follow the cycle
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True                      # Mark O(1)
                # Jump to the index where the current sorted position's element came from
                j = with_idx[j][1]                    # O(1)
                cycle_len += 1

            # A cycle of length L requires L-1 swaps
            if cycle_len > 0:
                swaps += cycle_len - 1                 # O(1)

        return swaps


# ----------------------------- OPTIONAL: second approach for parity -----------------------------
class SolutionGreedy:
    def minSwaps(self, arr: List[int]) -> int:
        """
        Greedy placement (equivalent to cycles, but more 'operational'):
        - Sort a copy to know which value should be at i.
        - If arr[i] is wrong, swap it with the position where its correct value currently is.
        - Update the value->index map in O(1).

        Time:  O(n log n)  (sort)
        Space: O(n)        (map)
        """
        n = len(arr)
        sorted_vals = sorted(arr)                         # O(n log n)
        pos = {v: i for i, v in enumerate(arr)}          # O(n)
        swaps = 0

        for i in range(n):                                # O(n)
            want = sorted_vals[i]
            if arr[i] == want:
                continue
            j = pos[want]                                # where the wanted value currently sits (O(1))

            # Single swap places at least one element correctly
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1

            # Update positions in O(1)
            pos[arr[j]] = j
            pos[arr[i]] = i

        return swaps


# ----------------------------- Tiny benchmarking helper -----------------------------
def bench(func, *args, number=1000):
    """
    Use timeit to measure average execution time.
    The lambda isolates the function call overhead nicely.

    Returns the average seconds per run (float).
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    avg = total / number
    return avg


# ----------------------------- Main Program (inputs, outputs, timings) -----------------------------
if __name__ == "__main__":
    tests = [
        # (input_array, expected_min_swaps)
        ([2, 8, 5, 4], 1),
        ([10, 19, 6, 3, 5], 2),
        ([1, 3, 4, 5, 6], 0),
        ([4, 3, 2, 1], 2),             # classic reverse: cycles (0<->3, 1<->2)
        ([7, 1, 3, 2, 4, 5, 6], 5),    # common test
    ]

    print("=== Minimum Swaps to Sort ===\n")

    solver = Solution()
    parity_solver = SolutionGreedy()

    for arr, expected in tests:
        arr_copy_1 = arr[:]              # keep originals for parity check
        arr_copy_2 = arr[:]

        # Run primary solution (doesn't mutate arr)
        ans = solver.minSwaps(arr_copy_1)
        print(f"Input: {arr}")
        print(f"Minimum swaps (Cycle method): {ans} | Expected: {expected}")

        # Parity check with greedy (mutates arr_copy_2)
        ans2 = parity_solver.minSwaps(arr_copy_2)
        print(f"Minimum swaps (Greedy place): {ans2}")
        print(f"Both methods agree? {ans == ans2}\n")

    # --------- Timings with timeit ---------
    print("=== Timings (average seconds per run) ===")
    sample_arr = [10, 19, 6, 3, 5]
    runs_small = 20000
    runs_medium = 5000

    t_cycle_small = bench(solver.minSwaps, sample_arr[:], number=runs_small)
    t_greedy_small = bench(parity_solver.minSwaps, sample_arr[:], number=runs_small)

    print(f"Input: {sample_arr}, runs={runs_small}")
    print(f"Cycle method avg: {t_cycle_small:.8e} s")
    print(f"Greedy method avg: {t_greedy_small:.8e} s")

    sample_arr2 = [7, 1, 3, 2, 4, 5, 6]
    t_cycle_med = bench(solver.minSwaps, sample_arr2[:], number=runs_medium)
    t_greedy_med = bench(parity_solver.minSwaps, sample_arr2[:], number=runs_medium)

    print(f"\nInput: {sample_arr2}, runs={runs_medium}")
    print(f"Cycle method avg: {t_cycle_med:.8e} s")
    print(f"Greedy method avg: {t_greedy_med:.8e} s")

    print("\nNote: Timing numbers vary by machine and Python version.")
```

### What the program does

* Prints each **input array**, the **minimum swaps** from the **cycle method**, the **greedy result**, and whether they agree.
* Uses `timeit` to show average runtime over many runs for two sample inputs.

---

## 6) Real-World Use Cases (the important ones)

1. **Rebalancing / Reassignment with Minimal Moves**
   When items (tasks, containers, VMs) must be rearranged to a target order/placement, modeling the current→target map as a permutation lets you compute the **fewest swaps/moves** to reach the desired configuration.

2. **Warehouse Slotting / Rack Optimization**
   To place SKUs in a precomputed optimal order (e.g., by demand), calculate the minimum number of pairwise swaps (forklift moves) to transform the current layout into the target—useful for planning limited-time re-slotting.

3. **Register Allocation / Memory Layout Rewrites**
   Compilers and systems sometimes need to permute variables/registers/blocks into a canonical order; counting minimum swaps informs the **least disruptive** sequence of rewrites or data moves.

4. **Data Cleanup & ETL Reordering**
   During ETL, when rows must be sorted to a canonical ordering but moving rows is costly (e.g., across shards), this model gives the **lower bound** and a plan to reach the target with minimal row swaps.
