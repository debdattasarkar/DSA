# Kth Smallest

**Difficulty:** Medium
**Accuracy:** 35.17%
**Submissions:** 715K+
**Points:** 4
**Average Time:** 25m

---

## Problem Statement

Given an array `arr[]` and an integer `k` where `k` is smaller than the size of the array, find the **kᵗʰ smallest** element in the given array.

**Follow up:** Don’t solve it using the inbuilt sort function.

---

## Examples

### Example 1

**Input:** `arr[] = [7, 10, 4, 3, 20, 15], k = 3`
**Output:** `7`
**Explanation:** 3rd smallest element in the given array is 7.

### Example 2

**Input:** `arr[] = [2, 3, 1, 20, 15], k = 4`
**Output:** `15`
**Explanation:** 4th smallest element in the given array is 15.

---

## Constraints

* `1 ≤ arr.size ≤ 10^6`
* `1 ≤ arr[i] ≤ 10^6`
* `1 ≤ k ≤ n`

---

## Expected Complexities

* **Time Complexity:** `O(n + max_element)`
* **Auxiliary Space:** `O(n + max_element)`

---

## Company Tags

VMWare • Accolite • Amazon • Microsoft • Snapdeal • Hike • Adobe • Google • ABCO • Cisco

---

## Topic Tags

Arrays • Searching • Sorting • Data Structures • Algorithms

---

## Related Interview Experiences

* Cisco Interview Experience Set 9 Experienced
* Vmware Interview Experience Set 4 Campus
* Abco Interview Experience Set 5
* Adobe Interview Experience Off Campus

---

## Related Articles

* Kth Largest Element in an Array
* Kth Smallest Largest Element in Unsorted Array Expected Linear Time
* Kth Smallest Largest Element in Unsorted Array Worst Case Linear Time
* Kth Smallest Largest Element in Unsorted Array

---

---

awesome — let’s nail the **k-th smallest** problem the way interviewers like it: crystal-clear logic, a quick dry run, and multiple solutions (Quickselect, Heap, Counting—since the constraints allow it).

---

# 2) Explanation + Step-by-Step Dry Run

### Problem

Given an array `arr` and an integer `k` (1-indexed), return the **k-th smallest** element.
Follow-up says: *don’t* just sort and pick, so we’ll focus on **Quickselect** (expected) plus **Heaps** and **Counting** (values ≤ 10^6).

### Approaches you should know

1. **Quickselect (expected average-linear)**

   * Like quicksort’s partition but only recurses into the side that contains the k-th item.
   * **Time:** Average `O(n)`, Worst `O(n^2)` (random pivot makes worst case unlikely).
   * **Space:** `O(1)` in-place (ignoring recursion if you code it recursively).

2. **Max-Heap of size k (great when k ≪ n)**

   * Keep the k smallest seen so far; top of max-heap is the current k-th smallest.
   * **Time:** `O(n log k)`; **Space:** `O(k)`.
   * In Python, `heapq` is a **min-heap**; we simulate max-heap with **negated values**.

3. **Counting (when values are small & non-negative)**

   * Build frequency array of size `U = max_value` (here `≤ 10^6`).
   * Walk counts until you consume `k`.
   * **Time:** `O(n + U)`, **Space:** `O(U)`. Very fast if `U` is manageable.

> Sorting (`O(n log n)`) is legal but fails the “don’t use sort” follow-up; still good as a baseline.

---

## Dry Run (Quickselect)

Input: `arr = [7, 10, 4, 3, 20, 15]`, `k = 3` (we want the 3rd smallest → index `k-1 = 2` in 0-based after partitioning)

We’ll use **Lomuto partition** and (say) a **random pivot**. Suppose pivot happens to be `7`.

1. **Partition around 7**

   * Move all `< 7` to the left, `≥ 7` to the right (Lomuto places pivot in its final position).
   * After partition, a possible array: `[4, 3, 7, 10, 20, 15]`
   * Pivot index = `2`.

2. Compare pivot index `2` with target index `2`

   * They match ⇒ **answer = 7** (3rd smallest).
   * Done in **one pass** over the array.

If pivot had landed left of 2, we’d recurse/select on the **right** subarray; if right of 2, on the **left** subarray—always only one side.

---

# 3) Python Solutions (clear variable names, inline comments)

I’ll make `Quickselect` the primary `kthSmallest`; then include **Heap** and **Counting** alternatives you can call if desired.

```python
# User function Template for python3
import random
import heapq
from typing import List

class Solution:
    def kthSmallest(self, arr: List[int], k: int) -> int:
        """
        Quickselect with 3-way partition (Dutch National Flag).
        Average time: O(n), worst-case: O(n^2) -- mitigated by random pivot
        Space: O(1) extra (in-place)
        """
        n = len(arr)
        if not (1 <= k <= n):
            raise ValueError("k out of bounds")

        # We want 0-based index
        target = k - 1
        low, high = 0, n - 1

        while True:
            if low == high:
                return arr[low]

            # --- choose a random pivot to avoid adversarial worst cases
            pivot_idx = random.randint(low, high)
            pivot = arr[pivot_idx]

            # 3-way partition around pivot: < pivot | == pivot | > pivot
            left, i, right = low, low, high
            while i <= right:
                if arr[i] < pivot:
                    arr[left], arr[i] = arr[i], arr[left]
                    left += 1; i += 1
                elif arr[i] > pivot:
                    arr[i], arr[right] = arr[right], arr[i]
                    right -= 1
                else:  # equal
                    i += 1

            # Now:
            # arr[low:left]   < pivot
            # arr[left:right+1] == pivot
            # arr[right+1:high+1] > pivot

            if target < left:
                high = left - 1                 # go left
            elif target > right:
                low = right + 1                 # go right
            else:
                return arr[target]          # inside the equal block → done

    # ----------------------- Alternative 1: Heap (max-heap of size k) -----------------------
    def kthSmallest_heap(self, arr: List[int], k: int) -> int:
        """
        Keep a max-heap (simulated with negatives) of size k containing the k smallest seen.
        Time  : O(n log k)
        Space : O(k)
        """
        if not arr or k < 1 or k > len(arr):
            raise ValueError("k out of bounds")

        max_heap = []  # will store negatives to simulate max-heap using heapq
        # Build with first k elements
        for value in arr[:k]:                     # O(k)
            heapq.heappush(max_heap, -value)     # O(log k)

        # Process remaining elements
        for value in arr[k:]:                     # O(n-k)
            if value < -max_heap[0]:             # if strictly smaller than current k-th smallest
                heapq.heapreplace(max_heap, -value)  # pop+push in O(log k)

        # Top of the max-heap is the k-th smallest
        return -max_heap[0]

    # ----------------------- Alternative 2: Counting (values up to 10^6) -----------------------
    def kthSmallest_counting(self, arr: List[int], k: int) -> int:
        """
        Counting approach when 0 <= arr[i] <= 10^6 (or generally small, non-negative range).
        Time  : O(n + U) where U = max(arr) + 1
        Space : O(U)
        """
        if not arr or k < 1 or k > len(arr):
            raise ValueError("k out of bounds")

        # If negatives can appear, you can offset indices; problem's constraints are positive.
        max_value = max(arr)  # O(n)
        counts = [0] * (max_value + 1)  # O(U) space

        # frequency count: O(n)
        for value in arr:
            counts[value] += 1

        # walk counts to find k-th element: O(U)
        remaining = k
        for value, freq in enumerate(counts):
            if freq == 0:
                continue
            if remaining > freq:
                remaining -= freq
            else:
                return value

        # If k valid, we should have returned
        raise RuntimeError("Unexpected state in counting")
```

### Complexity Recap

* **Quickselect (randomized):** Average **O(n)**, worst **O(n²)**; space **O(1)**.
* **Heap (size k):** **O(n log k)**, space **O(k)** — ideal when `k ≪ n`.
* **Counting:** **O(n + U)**, space **O(U)** — ideal when the value range is small (fits in memory).

---

# 4) Interviewer-Style Q&A

**Q1. Why not sort?**

Sorting is `O(n log n)` and touches elements more than needed. Quickselect gets average **O(n)** by discarding half the array each step.

**Q2. Quickselect worst case and how to avoid it?**

Worst case is `O(n²)` (e.g., always picking smallest/largest as pivot with already ordered data).
Use **randomized pivot** (as above) or **median-of-medians (BFPRT)** to guarantee `O(n)` worst-case (but more constants/complexity).

**Q3. How does Quickselect differ from Quicksort?**

Both partition. Quicksort recurses on **both** sides; Quickselect only recurses into the **side containing the k-th index**, making it linear on average.

**Q4. When is a heap better than Quickselect?**

When `k` is small relative to `n` and/or you’re in a **streaming** setting: maintain a **max-heap** of size `k` and update per item in `O(log k)`.

**Q5. What about duplicates?**

All approaches handle duplicates naturally. The k-th order statistic counts duplicates as distinct positions.

**Q6. Counting approach applicability?**

Use when values are **non-negative and bounded** with a **small range** `U` (e.g., ≤ 10^6). Complexity `O(n + U)` can beat Quickselect if `U` is small; memory is the limiter.

**Q7. Stability and order?**

We’re returning a single value (order statistic). Stability of sorting is irrelevant.

**Q8. Can you find k-th largest with same code?**

Yes. For Quickselect, target index becomes `n - k`. For heap, use a **min-heap of size k** to retain the k largest.

**Q9. What if `k` is out of bounds?**

Always validate `1 ≤ k ≤ n` and raise/handle errors accordingly.

---

---

awesome — here’s a **complete, runnable Python program** that:

* reads an array and `k` from stdin,
* computes the **k-th smallest** using three approaches (Quickselect, Heap, Counting),
* prints results,
* and times each method with both a **single wall-clock run** and a **`timeit` average**.

Every major line is annotated with **time/space complexity**.

---

## Full Program (copy–paste and run)

```python
#!/usr/bin/env python3
"""
K-th Smallest Element in an Unsorted Array
- Primary: Randomized Quickselect (avg O(n), in-place)
- Alternatives: Max-Heap of size k (O(n log k)), Counting (O(n + U))
Input:
  Line 1: space-separated integers (array)
  Line 2: single integer k  (1-indexed)
Example:
  7 10 4 3 20 15
  3
Output:
  Kth Smallest (Quickselect) : 7
  ... (with timing)
"""

from typing import List
import random
import heapq
from time import perf_counter
import timeit
import sys


# ------------------------------------------------------------
# Core solution class
# ------------------------------------------------------------
class Solution:
    # ---------- Primary: Quickselect (average O(n), in-place O(1) space) ----------
    def kthSmallest(self, arr: List[int], k: int) -> int:
        """
        Randomized Quickselect to find k-th smallest (1-indexed).
        Time : Average O(n), Worst O(n^2) (mitigated by random pivot)
        Space: O(1) auxiliary (iterative)
        """
        if not arr or k < 1 or k > len(arr):
            raise ValueError("k out of bounds")

        target_index = k - 1            # O(1)
        left, right = 0, len(arr) - 1   # O(1)

        # Iterative quickselect keeps memory O(1)
        while left <= right:            # Expected O(n) total work
            # --- choose a random pivot to avoid adversarial inputs (O(1)) ---
            pivot_index = random.randint(left, right)
            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  # move pivot to end (O(1))

            # --- Lomuto partition around pivot_value in one linear pass ---
            pivot_value = arr[right]    # O(1)
            store_index = left          # where next smaller element goes
            for i in range(left, right):           # O(right-left+1) per iteration
                if arr[i] < pivot_value:
                    arr[i], arr[store_index] = arr[store_index], arr[i]  # O(1)
                    store_index += 1

            # put pivot into its final sorted location
            arr[store_index], arr[right] = arr[right], arr[store_index]  # O(1)

            # --- Decide which side to continue searching (O(1)) ---
            if store_index == target_index:
                return arr[store_index]
            elif store_index < target_index:
                left = store_index + 1
            else:
                right = store_index - 1

        # If k valid, we must have returned
        raise RuntimeError("Unexpected state in quickselect")

    # ---------- Alternative: Max-Heap of size k (O(n log k), O(k) space) ----------
    def kthSmallest_heap(self, arr: List[int], k: int) -> int:
        """
        Maintain the k smallest elements in a max-heap (via negation).
        Time : O(n log k)  [heap push/replace is log k]
        Space: O(k)
        """
        if not arr or k < 1 or k > len(arr):
            raise ValueError("k out of bounds")

        max_heap = []                            # O(1)
        for value in arr[:k]:                    # O(k)
            heapq.heappush(max_heap, -value)     # O(log k)

        for value in arr[k:]:                    # O(n - k)
            if value < -max_heap[0]:             # O(1) compare against current k-th smallest
                heapq.heapreplace(max_heap, -value)  # pop+push O(log k)

        return -max_heap[0]

    # ---------- Alternative: Counting (O(n + U), O(U) space) ----------
    def kthSmallest_counting(self, arr: List[int], k: int) -> int:
        """
        Counting approach when values are bounded and non-negative (here ≤ 10^6).
        Time : O(n + U) where U = max(arr) + 1
        Space: O(U)
        """
        if not arr or k < 1 or k > len(arr):
            raise ValueError("k out of bounds")

        max_value = max(arr)             # O(n)
        counts = [0] * (max_value + 1)   # O(U) space

        for value in arr:                # O(n)
            # If negatives can exist, offset the index; constraints often say ≥ 1.
            counts[value] += 1

        remaining = k                    # O(1)
        for value, freq in enumerate(counts):  # O(U)
            if freq == 0: 
                continue
            if remaining > freq:
                remaining -= freq
            else:
                return value

        raise RuntimeError("Unexpected state in counting")


# ------------------------------------------------------------
# Timing helpers
# ------------------------------------------------------------
def time_single_run(func, *args, **kwargs):
    """Single wall-clock timing using perf_counter."""
    t0 = perf_counter()
    result = func(*args, **kwargs)
    t1 = perf_counter()
    return result, (t1 - t0)

def time_with_timeit(callable_stmt, number=5):
    """Average runtime over `number` runs using timeit."""
    total = timeit.timeit(callable_stmt, number=number)
    return total / number


# ------------------------------------------------------------
# Main driver
# ------------------------------------------------------------
def main():
    # ---------- Parse input ----------
    data = sys.stdin.read().strip().split()
    if not data:
        print("No input provided.\nExample:\n  7 10 4 3 20 15\n  3")
        return
    *arr_tokens, k_token = data[:-1], data[-1]  # handle case of two lines or one line carefully
    # If user pasted in two lines, data already split. We need to detect where array ends:
    # Safer: read two lines explicitly if available:

    # Try to interpret last token as k; if that fails, fallback to two-line parse.
    try:
        k = int(k_token)
        # everything before last token is the array
        arr = list(map(int, data[:-1]))
    except ValueError:
        # Fallback: assume two lines; first line is array, second is k
        lines = " ".join(data).splitlines()
        arr = list(map(int, lines[0].split()))
        k = int(lines[1].strip())

    print("Array:", arr)
    print("k    :", k)

    solver = Solution()

    # ---------- Quickselect ----------
    qs_val, qs_time = time_single_run(solver.kthSmallest, arr.copy(), k)
    qs_avg = time_with_timeit(lambda: solver.kthSmallest(arr.copy(), k), number=5)
    print(f"\nKth Smallest (Quickselect) : {qs_val}")
    print(f"  Single-run time : {qs_time:.8f} s")
    print(f"  Avg over 5 runs : {qs_avg:.8f} s")

    # ---------- Heap ----------
    hp_val, hp_time = time_single_run(solver.kthSmallest_heap, arr, k)  # arr not mutated
    hp_avg = time_with_timeit(lambda: solver.kthSmallest_heap(arr, k), number=5)
    print(f"\nKth Smallest (Heap k={k})  : {hp_val}")
    print(f"  Single-run time : {hp_time:.8f} s")
    print(f"  Avg over 5 runs : {hp_avg:.8f} s")

    # ---------- Counting ----------
    # If values are non-negative and reasonably bounded, counting is viable.
    can_counting = min(arr) >= 0
    if can_counting:
        ct_val, ct_time = time_single_run(solver.kthSmallest_counting, arr, k)
        ct_avg = time_with_timeit(lambda: solver.kthSmallest_counting(arr, k), number=5)
        print(f"\nKth Smallest (Counting)    : {ct_val}")
        print(f"  Single-run time : {ct_time:.8f} s")
        print(f"  Avg over 5 runs : {ct_avg:.8f} s")
    else:
        print("\nKth Smallest (Counting)    : skipped (array has negatives; add offset if needed)")

    # ---------- Complexity summary ----------
    print("\nComplexity Summary:")
    print("  Quickselect : Time avg O(n), worst O(n^2); Space O(1)")
    print("  Heap       : Time O(n log k);                Space O(k)")
    print("  Counting   : Time O(n + U);                   Space O(U)  (U = max(arr)+1)")


if __name__ == "__main__":
    """
    Example run:
      echo -e "7 10 4 3 20 15\n3" | python3 kth_smallest.py
    Expected:
      Kth Smallest ... : 7
    """
    main()
```

### Example run

Input

```
7 10 4 3 20 15
3
```

Output (times will vary):

```
Array: [7, 10, 4, 3, 20, 15]
k    : 3

Kth Smallest (Quickselect) : 7
  Single-run time : 0.00007xx s
  Avg over 5 runs : 0.00006xx s

Kth Smallest (Heap k=3)  : 7
  Single-run time : 0.00010xx s
  Avg over 5 runs : 0.00010xx s

Kth Smallest (Counting)    : 7
  Single-run time : 0.00004xx s
  Avg over 5 runs : 0.00004xx s

Complexity Summary:
  Quickselect : Time avg O(n), worst O(n^2); Space O(1)
  Heap       : Time O(n log k);                Space O(k)
  Counting   : Time O(n + U);                   Space O(U)  (U = max(arr)+1)
```

---

## 6) Real-World Use Cases (high-impact)

* **Percentiles & SLOs (P50/P90/P99):** The k-th order statistic directly powers latency/throughput percentile calculations without fully sorting (Quickselect/Heap are ideal).
* **Streaming top-k / thresholding:** Maintain the **k smallest/largest** elements in real-time (max/min-heap of size k) for dashboards and anomaly detection.
* **Approximate selection in big data:** Pre-filter or partition large datasets, then **Quickselect** on partitions to find medians/quantiles faster than full sort.
* **Robotics & Vision:** Choose **k nearest** distances (k-NN pre-steps) or thresholds in sensor fusion using selection without sorting all readings.

> In interviews: implement **Quickselect** confidently, mention **Heap** for streaming / small k, and **Counting** when the value range is small and bounded.
