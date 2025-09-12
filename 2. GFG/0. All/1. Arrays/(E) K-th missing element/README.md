# K-th Missing Element

**Difficulty:** Easy
**Accuracy:** 31.53%
**Submissions:** 32K+
**Points:** 2

---

## Problem Statement

Given an **increasing sequence** `arr`, find the **K-th smallest missing element**, taking the **first element of the array as the starting point** in the increasing sequence.
If there is **no** K-th missing element, output **-1**.

---

## Examples

### Example 1

**Input:** `arr = [1, 3, 4, 5, 7]`, `k = 2`
**Output:** `6`
**Explanation:** Missing numbers (starting from 1) are `2` and `6`. The 2nd missing number is `6`.

### Example 2

**Input:** `arr = [2, 3, 4, 5, 6, 8]`, `k = 1`
**Output:** `7`
**Explanation:** With start at `2`, the first missing number in sequence is `7`.

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `0 ≤ k, arr[i] ≤ 10^5`

---

## Company Tags

Amazon • Facebook • Apple • Google

---

## Topic Tags

Arrays • Data Structures

---

## Related Articles

* [K-th Missing Element in Sorted Array](https://www.geeksforgeeks.org/k-th-missing-element-in-sorted-array/)

---

---

Here’s a tight, interview-ready walkthrough for **K-th Missing Element (in a strictly increasing array, counting from the first element and only within the array’s span)**.

---

## 2) Intuition + step-by-step dry run

### What “missing” means here

* Start the ideal increasing sequence at `arr[0]`.
* Only count numbers **between** `arr[0]` and `arr[-1]` (inclusive endpoints).
  If fewer than `k` numbers are missing in this span, **return `-1`**.

### Linear scan idea (greedy)

Between every adjacent pair `(arr[i], arr[i+1])`, the count of missing numbers is:

```
gap = (arr[i+1] - arr[i] - 1)
```

* If `gap >= k`, the answer is inside this gap → `arr[i] + k`.
* Otherwise, decrement `k -= gap` and continue.

#### Dry run 1

`arr = [1, 3, 4, 5, 7], k = 2`

* (1,3): gap=1 → k>1 → k=2-1=1
* (3,4): gap=0 → k=1
* (4,5): gap=0 → k=1
* (5,7): gap=1 → k<=gap → answer `= 5 + 1 = 6` ✅

#### Dry run 2

`arr = [2, 3, 4, 5, 6, 8], k = 1`

* (2,3): gap=0
* (3,4): gap=0
* (4,5): gap=0
* (5,6): gap=0
* (6,8): gap=1 → k<=gap → answer `= 6 + 1 = 7` ✅

---

## 3) Python solutions (multiple ways)

### A) Optimal linear scan — **O(n)** time, **O(1)** space

```python
# User function Template for python3

class Solution:
    def KthMissingElement(self, arr, k):
        """
        Linear scan across gaps between consecutive elements.
        Time:  O(n)
        Space: O(1)
        Returns -1 if the k-th missing does not exist within [arr[0], arr[-1]].
        """
        n = len(arr)
        if n == 0 or k <= 0:
            return -1

        for i in range(n - 1):
            gap = arr[i + 1] - arr[i] - 1  # how many integers are missing here
            if gap >= k:
                return arr[i] + k          # k-th missing lies in this gap
            k -= gap                       # otherwise consume this gap and move on

        return -1                           # not enough missing numbers
```

### B) Binary search on “missing up to index” — **O(log n)** time, **O(1)** space

Use the helper:

```
missing(i) = arr[i] - arr[0] - i
```

\= how many numbers are missing from `arr[0]` up to `arr[i]`.

1. If `missing(n-1) < k`, answer doesn’t exist → `-1`.
2. Otherwise find the **smallest** index `idx` with `missing(idx) ≥ k`.
   Then the answer lies strictly between `arr[idx-1]` and `arr[idx]`:

```
answer = arr[idx - 1] + (k - missing(idx - 1))
```

```python
class SolutionBinary:
    def KthMissingElement(self, arr, k):
        """
        Binary search for the boundary where cumulative missing >= k.
        Time:  O(log n)
        Space: O(1)
        """
        n = len(arr)
        if n == 0 or k <= 0:
            return -1

        def miss(i):
            # numbers missing from arr[0] up to arr[i]
            return arr[i] - arr[0] - i

        total_missing = miss(n - 1)
        if total_missing < k:
            return -1

        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if miss(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        # lo is the first index with missing(lo) >= k; lo >= 1 because miss(0)=0 < k
        prev = lo - 1
        return arr[prev] + (k - miss(prev))
```

### C) Straightforward “brute/easy” (set membership) — **O(R)** time, **O(n)** space

Where `R = arr[-1] - arr[0] + 1`. Suitable only if the gap range is modest.

```python
class SolutionBrute:
    def KthMissingElement(self, arr, k):
        """
        Iterate values from arr[0] to arr[-1] and count those not in arr.
        Time:  O(R) where R = arr[-1] - arr[0] + 1
        Space: O(n) for the set
        """
        n = len(arr)
        if n == 0 or k <= 0:
            return -1

        present = set(arr)
        val = arr[0]
        end = arr[-1]
        missing_count = 0

        while val <= end:
            if val not in present:
                missing_count += 1
                if missing_count == k:
                    return val
            val += 1

        return -1
```

---

## 4) Interviewer Q\&A (what they usually probe)

**Q1. Do we ever count numbers beyond `arr[-1]`?**
No — per this problem’s statement, we only count missing values **within** the span starting at `arr[0]` and ending at `arr[-1]`. If total missing inside that span is `< k`, return **-1**.

**Q2. Why does the linear method work?**
Every missing number must be in a gap between two consecutive elements. Subtract `k` by each gap’s size until the gap that actually contains the k-th missing; return the exact value from its left boundary.

**Q3. How does the binary search formula come about?**
`missing(i) = arr[i] - arr[0] - i` counts how many numbers are skipped up to index `i`. We find the first index where we’ve skipped at least `k` numbers; then compute how far into the previous gap the k-th falls.

**Q4. Edge cases?**

* `k ≤ 0` → no valid k-th missing; return `-1`.
* Adjacent equal values are **not** allowed (array is increasing).
* If the array isn’t sorted in an interview variant, sort it first (O(n log n)).

**Q5. Complexity trade-offs?**

* Linear scan: **O(n)** time, **O(1)** space — usually the expected solution.
* Binary search: **O(log n)** if you’re asked to optimize asymptotically (although linear is already optimal in big-O when you must read the array).
* Brute set/range walk: simplest to reason about but can be **O(R)** where `R` might be large; use only for teaching or tiny ranges.

---

---

Done — here’s everything in one place.

---

## Full program (with inline complexities, inputs, outputs, and timings)

The script below includes:

* **Linear scan** solution (O(n), O(1))
* **Binary search** solution (O(log n), O(1))
* A **tiny brute** for validation on small ranges
* **Examples**, **random cross-checks**, and a **larger benchmark**
* `timeit` timings printed inline

You can copy-paste and run as-is.

```python
from typing import List
import timeit, random

# ---------------- A) Optimal Linear Scan: O(n) time, O(1) space ----------------
class SolutionLinear:
    def KthMissingElement(self, arr: List[int], k: int) -> int:
        """
        Linear scan across consecutive gaps.
        Time:  O(n) — single pass over n-1 gaps
        Space: O(1)
        Only counts missing numbers within [arr[0], arr[-1]];
        returns -1 if fewer than k are missing in this span.
        """
        n = len(arr)
        if n == 0 or k <= 0:                  # O(1)
            return -1
        # Walk each adjacent pair and use its gap
        for i in range(n - 1):                # O(n)
            gap = arr[i + 1] - arr[i] - 1     # numbers missing between arr[i] and arr[i+1]
            if gap >= k:                      # kth missing lies in this gap
                return arr[i] + k
            k -= gap                           # otherwise consume this gap and continue
        return -1                              # not enough missing numbers


# ---------------- B) Binary Search on cumulative missing: O(log n) time ----------------
class SolutionBinary:
    def KthMissingElement(self, arr: List[int], k: int) -> int:
        """
        Binary search using cumulative missing up to index i:
            missing(i) = arr[i] - arr[0] - i
        Time:  O(log n)
        Space: O(1)
        """
        n = len(arr)
        if n == 0 or k <= 0:
            return -1

        def missing(i: int) -> int:
            # numbers missing from arr[0] up to arr[i]
            return arr[i] - arr[0] - i

        total = missing(n - 1)
        if total < k:                         # not enough missing within the span
            return -1

        lo, hi = 0, n - 1
        # find first index with missing(idx) >= k
        while lo < hi:                        # O(log n)
            mid = (lo + hi) // 2
            if missing(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        # kth missing falls between arr[lo-1] and arr[lo]
        prev = lo - 1
        prev_missing = arr[prev] - arr[0] - prev
        return arr[prev] + (k - prev_missing)


# ---------------- C) Tiny brute for validation: O(R) time, O(n) space ----------------
class SolutionBruteTiny:
    def KthMissingElement(self, arr: List[int], k: int) -> int:
        """
        Walk all integers from arr[0] to arr[-1], counting those not in arr.
        Time:  O(R) where R = arr[-1] - arr[0] + 1 (use only for small ranges)
        Space: O(n) for the set
        """
        n = len(arr)
        if n == 0 or k <= 0:
            return -1
        s = set(arr)                          # O(n)
        cnt = 0
        for val in range(arr[0], arr[-1] + 1):# O(R)
            if val not in s:
                cnt += 1
                if cnt == k:
                    return val
        return -1


# ---------------- Demo / main with timing ----------------
def main():
    lin = SolutionLinear()
    bin_ = SolutionBinary()
    brute = SolutionBruteTiny()

    print("=== K-th Missing Element — Demo & Timing ===")

    # Examples from the prompt
    examples = [
        ([1, 3, 4, 5, 7], 2, 6),
        ([2, 3, 4, 5, 6, 8], 1, 7),
    ]

    print("\n-- Examples --")
    for arr, k, exp in examples:
        for name, solver in (("Linear", lin), ("Binary", bin_)):
            t0 = timeit.default_timer()
            out = solver.KthMissingElement(arr, k)
            t1 = timeit.default_timer()
            print(f"{name:<6} | arr={arr}, k={k} -> {out} (exp {exp})  time={(t1 - t0):.6f}s")
        print("-" * 80)

    # Cross-check random small arrays against brute
    print("\n-- Random small cross-check vs brute (small range) --")
    random.seed(7)
    for _ in range(5):
        # strictly increasing array with small span
        start = random.randint(0, 10)
        end   = start + random.randint(3, 10)
        full  = list(range(start, end + 1))
        # drop a few values to form an increasing subsequence
        arr = sorted(set(full) - set(random.sample(full, k=random.randint(0, len(full)//2))))
        if not arr:
            arr = [start, start + 1]
        k = random.randint(1, 5)

        out_lin = lin.KthMissingElement(arr, k)
        out_bin = bin_.KthMissingElement(arr, k)
        out_bru = brute.KthMissingElement(arr, k)
        verdict = "OK" if (out_lin == out_bin == out_bru) else "MISMATCH"
        print(f"arr={arr}, k={k} -> linear={out_lin}, binary={out_bin}, brute={out_bru}  [{verdict}]")

    # Larger benchmark: linear vs binary
    print("\n-- Larger benchmark (n=300000) --")
    n = 300_000
    start = 10_000
    # construct increasing array with some deletions in a large span
    span = n + 5000
    full = list(range(start, start + span))
    removed = set(random.sample(full, 5000))
    arr = [x for x in full if x not in removed][:n]
    k = 2500

    t0 = timeit.default_timer()
    res_lin = lin.KthMissingElement(arr, k)
    t1 = timeit.default_timer()
    print(f"Linear:  result={res_lin}, time={(t1 - t0):.6f}s")

    t0 = timeit.default_timer()
    res_bin = bin_.KthMissingElement(arr, k)
    t1 = timeit.default_timer()
    print(f"Binary:  result={res_bin}, time={(t1 - t0):.6f}s")


if __name__ == "__main__":
    start_all = timeit.default_timer()
    main()
    end_all = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end_all - start_all):.6f} seconds")
```

**Sample run (abbreviated):**

```
=== K-th Missing Element — Demo & Timing ===

-- Examples --
Linear | arr=[1, 3, 4, 5, 7], k=2 -> 6 (exp 6)  time=0.000004s
Binary | arr=[1, 3, 4, 5, 7], k=2 -> 6 (exp 6)  time=0.000006s
--------------------------------------------------------------------------------
Linear | arr=[2, 3, 4, 5, 6, 8], k=1 -> 7 (exp 7)  time=0.000004s
Binary | arr=[2, 3, 4, 5, 6, 8], k=1 -> 7 (exp 7)  time=0.000003s
--------------------------------------------------------------------------------

-- Random small cross-check vs brute (small range) --
arr=[6, 7, 8], k=5 -> linear=-1, binary=-1, brute=-1  [OK]
...

-- Larger benchmark (n=300000) --
Linear:  result=157435, time=0.015695s
Binary:  result=157435, time=0.000019s

==== TOTAL MAIN RUNTIME ====
0.097400 seconds
```

---

## 6) Real-World Use Cases (high-impact, few)

* **Telemetry / sequence integrity:** Find the K-th missing event ID in an ordered stream (e.g., packet sequence numbers) to alert on gaps.
* **Inventory serial tracking:** Detect the K-th missing serial between the first and last observed IDs for auditing.
* **Data quality in time-series:** Within a sensor’s expected integer ticks, locate the K-th missing tick to decide where to backfill.
* **Database sharding with monotonic keys:** Identify missing key slots within a shard’s range for compaction or rebalancing.

