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

Here’s a compact, interview-ready guide to the **Kth Smallest Element** problem.

---

## 2) Intuition + step-by-step dry run

We want the element that would sit at index `k-1` if the array were sorted (0-based).

### Main idea (Quickselect)

Quickselect is like quicksort but only explores the side that contains the k-th element.

1. Pick a **pivot**.
2. **Partition** the array so that:

   * elements `< pivot` are to the left,
   * elements `== pivot` are in the middle,
   * elements `> pivot` are to the right.
3. If `k-1` falls in the left part → recurse left;
   if it falls in the middle block → we’re done;
   else recurse right (with adjusted k).

Average time **O(n)**, in-place, **O(1)** extra space. Worst case **O(n²)** (mitigated by random/median-of-three pivot).

### Dry run (Quickselect, 3-way partition)

`arr = [7, 10, 4, 3, 20, 15], k = 3` → target index `t = 2`.

Assume pivot chosen is `7`.

Partition around `7`:

* `<7`: `[4, 3]`
* `==7`: `[7]`
* `>7`: `[10, 20, 15]`

Sizes: L=2, E=1.
Indices:

* Left covers `[0..1]`
* Equal covers `[2..2]`  ← target `t=2` falls **here**
  Answer = `7`.

(If `t` had fallen in the left or right block, we’d recurse only into that side.)

---

## 3) Python solutions (with interview-style comments)

I’m giving **four** approaches:

* A) **Quickselect** (expected; average O(n), O(1) space)
* B) **Max-heap of size k** (O(n log k), O(k) space) — great when k ≪ n
* C) **Counting / bucket** (O(n + max\_val), O(max\_val)) — perfect when values are small & non-negative
* D) **Brute force sort** (O(n log n)) — simplest baseline (but discouraged in follow-up)

### A) Quickselect (default implementation for the given signature)

```python
# User function Template for python3
import random

class Solution:
    def kthSmallest(self, arr, k):
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
        lo, hi = 0, n - 1

        while True:
            if lo == hi:
                return arr[lo]

            # --- choose a random pivot to avoid adversarial worst cases
            pivot_idx = random.randint(lo, hi)
            pivot = arr[pivot_idx]

            # 3-way partition around pivot: < pivot | == pivot | > pivot
            lt, i, gt = lo, lo, hi
            while i <= gt:
                if arr[i] < pivot:
                    arr[lt], arr[i] = arr[i], arr[lt]
                    lt += 1; i += 1
                elif arr[i] > pivot:
                    arr[i], arr[gt] = arr[gt], arr[i]
                    gt -= 1
                else:  # equal
                    i += 1

            # Now:
            # arr[lo:lt]   < pivot
            # arr[lt:gt+1] == pivot
            # arr[gt+1:hi+1] > pivot

            if target < lt:
                hi = lt - 1                 # go left
            elif target > gt:
                lo = gt + 1                 # go right
            else:
                return arr[target]          # inside the equal block → done
```

### B) Max-heap of size k (good when k ≪ n)

```python
import heapq

class SolutionHeapK:
    def kthSmallest(self, arr, k):
        """
        Maintain a max-heap of size k with the k smallest seen so far.
        Python has only a min-heap; simulate max-heap by pushing negatives.
        Time: O(n log k), Space: O(k)
        """
        if not (1 <= k <= len(arr)):
            raise ValueError("k out of bounds")
        heap = []
        for x in arr:
            if len(heap) < k:
                heapq.heappush(heap, -x)
            else:
                if x < -heap[0]:
                    heapq.heapreplace(heap, -x)
        # top of max-heap is the kth smallest (negate back)
        return -heap[0]
```

### C) Counting / Bucket (when values are small non-negative)

> Matches the “expected complexity” line from the prompt: **O(n + max\_element)** time, **O(n + max\_element)** space.

```python
class SolutionCounting:
    def kthSmallest(self, arr, k):
        """
        Counting approach. Works well if all numbers are integers in [0..M]
        with reasonably small M (e.g., up to ~1e6 as in the prompt).
        Time: O(n + max_val), Space: O(max_val)
        """
        if not (1 <= k <= len(arr)):
            raise ValueError("k out of bounds")
        if not arr:
            raise ValueError("empty array")

        max_val = max(arr)
        # If negatives exist, either shift them or use a dict counter instead.
        if min(arr) < 0:
            # Use dictionary count for general integers (O(n)), then sweep keys.
            from collections import Counter
            freq = Counter(arr)
            running = 0
            for v in sorted(freq.keys()):
                running += freq[v]
                if running >= k:
                    return v
        else:
            freq = [0] * (max_val + 1)
            for x in arr:
                freq[x] += 1
            running = 0
            for val, c in enumerate(freq):
                if c:
                    running += c
                    if running >= k:
                        return val
```

### D) Brute force (sort)

```python
class SolutionSort:
    def kthSmallest(self, arr, k):
        """
        Baseline: sort and index.
        Time: O(n log n), Space: O(1) to O(n) depending on sort implementation
        (Follow-up says: avoid using built-in sort as your primary solution.)
        """
        if not (1 <= k <= len(arr)):
            raise ValueError("k out of bounds")
        arr_sorted = sorted(arr)
        return arr_sorted[k - 1]
```

---

## 4) Interviewer Q\&A (the hits)

**Q1. Why Quickselect for kth order statistic?**
Because it delivers **expected O(n)** time and **O(1)** extra space, better than the O(n log n) of sorting.

**Q2. How do you avoid Quickselect’s worst case?**
Use a **random pivot** (as above) or **median-of-medians** pivot for guaranteed **O(n)** worst-case (but more complex constant factors).

**Q3. When would you prefer a heap?**
If **k is much smaller than n** or the input is a stream: maintain a **max-heap of size k** → **O(n log k)**.

**Q4. When is counting a good idea?**
When values are **integers in a small range** (e.g., `[0..1e6]`). Then **O(n + max\_val)** is very fast and simple.

**Q5. Duplicates?**
All methods handle duplicates naturally. For Quickselect 3-way partitioning helps a lot by collapsing `== pivot` into a block in one pass.

**Q6. Negative numbers?**
Quickselect/heap/sort: no issue. Counting: either **shift** values to be non-negative or use a **dict Counter** and sweep sorted keys.

**Q7. Stability / returning index vs. value?**
Problem asks for the **value**. If index is needed, adapt the partition/heap to keep track of original indices.

**Q8. Space/Time trade-offs summary?**

* Quickselect: avg O(n) / O(1) space (best general choice).
* Heap (size k): O(n log k) / O(k) (great for small k or streaming).
* Counting: O(n + R) / O(R) where R is range size (great when range is small).
* Sort: O(n log n) / built-in convenience (baseline, but not preferred).

---

---

Done! You’ve got a **complete, runnable program** that:

* Implements four interview-friendly solutions: **Quickselect (avg O(n))**, **Heap of size k (O(n log k))**, **Counting/Bucket** (O(n+R) when sensible), and a **Sort baseline**.
* Runs **prompt examples**, **random cross-checks**, and **benchmarks** with **timeit**.
* Prints **inputs, outputs, and timings**, plus a **total runtime** at the end.

```python

# Re-run to display outputs after the reset
from typing import List
import random, heapq, timeit
from collections import Counter
from array import array

class SolutionQuickselect:
    def kthSmallest(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if not (1 <= k <= n):
            raise ValueError("k out of bounds")
        target = k - 1
        lo, hi = 0, n - 1
        while True:
            if lo == hi:
                return arr[lo]
            pivot = arr[random.randint(lo, hi)]
            lt, i, gt = lo, lo, hi
            while i <= gt:
                if arr[i] < pivot:
                    arr[lt], arr[i] = arr[i], arr[lt]
                    lt += 1; i += 1
                elif arr[i] > pivot:
                    arr[i], arr[gt] = arr[gt], arr[i]
                    gt -= 1
                else:
                    i += 1
            if target < lt:
                hi = lt - 1
            elif target > gt:
                lo = gt + 1
            else:
                return arr[target]

class SolutionHeapK:
    def kthSmallest(self, arr: List[int], k: int) -> int:
        if not (1 <= k <= len(arr)):
            raise ValueError("k out of bounds")
        h = []
        for x in arr:
            if len(h) < k:
                heapq.heappush(h, -x)
            else:
                if x < -h[0]:
                    heapq.heapreplace(h, -x)
        return -h[0]

class SolutionCounting:
    def kthSmallest(self, arr: List[int], k: int) -> int:
        if not (1 <= k <= len(arr)):
            raise ValueError("k out of bounds")
        mn, mx = min(arr), max(arr)
        if mn < 0 or mx > 2_000_000:
            freq = Counter(arr)
            running = 0
            for v in sorted(freq.keys()):
                running += freq[v]
                if running >= k:
                    return v
        else:
            R = mx - mn + 1
            freq = array('I', [0]) * R
            for x in arr:
                freq[x - mn] += 1
            running = 0
            for i, c in enumerate(freq):
                if c:
                    running += c
                    if running >= k:
                        return i + mn

class SolutionSort:
    def kthSmallest(self, arr: List[int], k: int) -> int:
        if not (1 <= k <= len(arr)):
            raise ValueError("k out of bounds")
        return sorted(arr)[k - 1]

def main():
    qs  = SolutionQuickselect()
    hp  = SolutionHeapK()
    cnt = SolutionCounting()
    srt = SolutionSort()

    print("=== Kth Smallest — Demo & Timing ===")

    examples = [
        ([7, 10, 4, 3, 20, 15], 3, 7),
        ([2, 3, 1, 20, 15], 4, 15),
    ]
    print("\n-- Examples --")
    for arr, k, exp in examples:
        for name, solver in (("Quickselect", qs), ("Heap(k)", hp), ("Counting", cnt), ("Sort", srt)):
            a = arr[:]
            t0 = timeit.default_timer()
            out = solver.kthSmallest(a, k)
            t1 = timeit.default_timer()
            print(f"{name:<11} | arr={arr}, k={k} -> {out} (exp {exp})  time={(t1 - t0):.6f}s")
        print("-" * 90)

    print("\n-- Random small cross-check (all methods should agree) --")
    random.seed(42)
    for _ in range(5):
        n  = random.randint(8, 14)
        k  = random.randint(1, n)
        arr = [random.randint(-20, 30) for _ in range(n)]
        gold = srt.kthSmallest(arr[:], k)
        out_qs  = qs.kthSmallest(arr[:], k)
        out_hp  = hp.kthSmallest(arr[:], k)
        out_cnt = cnt.kthSmallest(arr[:], k)
        print(f"n={n:2d}, k={k:2d} | gold={gold}, quick={out_qs}, heap={out_hp}, count={out_cnt}")

    print("\n-- Large benchmark (n=200000, k random) --")
    n = 200_000
    random.seed(7)
    big = [random.randint(-10**6, 10**6) for _ in range(n)]
    k   = random.randint(1, n)
    a = big[:]
    t0 = timeit.default_timer()
    ans_qs = qs.kthSmallest(a, k)
    t1 = timeit.default_timer()
    print(f"Quickselect: ans={ans_qs}, time={(t1 - t0):.6f}s")
    a = big[:]
    t0 = timeit.default_timer()
    ans_hp = hp.kthSmallest(a, k)
    t1 = timeit.default_timer()
    print(f"Heap(k)    : ans={ans_hp}, time={(t1 - t0):.6f}s")

    print("\n-- Medium dense non-negative benchmark for Counting (n=300000, values in [0..200000]) --")
    n2 = 300_000
    random.seed(8)
    dense = [random.randint(0, 200_000) for _ in range(n2)]
    k2 = random.randint(1, n2)
    a = dense[:]
    t0 = timeit.default_timer()
    ans_cnt = cnt.kthSmallest(a, k2)
    t1 = timeit.default_timer()
    print(f"Counting   : ans={ans_cnt}, time={(t1 - t0):.6f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (high-impact)

* **Top-K analytics / dashboards:** Find the k-th threshold—e.g., the “k-th smallest latency”—to set SLOs (e.g., p95, p99 with slight modifications).
* **Memory-bounded streaming:** Maintain a **max-heap of size k** to track the k smallest values in a live stream (sensor data, logs) with fixed memory.
* **Scheduling & resource allocation:** Choose the **k-th earliest** deadline/arrival time to cut off acceptance or plan batches.
* **Quantile approximation building block:** Quickselect is the primitive behind many order-statistic tasks (median, quartiles) used in data pipelines.
* **Anomaly thresholds:** Use counting (when range is small) to quickly compute order statistics for real-time thresholds in telemetry with bounded value domains.
