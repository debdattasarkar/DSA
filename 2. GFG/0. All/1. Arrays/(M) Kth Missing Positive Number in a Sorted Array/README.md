# Kth Missing Positive Number in a Sorted Array

**Difficulty:** Medium
**Accuracy:** 53.02%
**Submissions:** 42K+
**Points:** 4

---

## Problem Statement

Given a **sorted** array of **distinct positive integers** `arr[]`, find the **k-th positive number** that is **missing** from `arr[]`.

---

## Examples

### Example 1

**Input:** `arr = [2, 3, 4, 7, 11], k = 5`
**Output:** `9`
**Explanation:** Missing positives are `1, 5, 6, 8, 9, 10, ...` and the 5th missing number is **9**.

### Example 2

**Input:** `arr = [1, 2, 3], k = 2`
**Output:** `5`
**Explanation:** Missing positives are `4, 5, 6, ...` and the 2nd missing number is **5**.

### Example 3

**Input:** `arr = [3, 5, 9, 10, 11, 12], k = 2`
**Output:** `2`
**Explanation:** Missing positives are `1, 2, 4, 6, ...` and the 2nd missing number is **2**.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ k ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(log n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* `Binary Search` • `Arrays`

---

## Related Articles

* [K-th Missing Element in Sorted Array](https://www.geeksforgeeks.org/k-th-missing-element-in-sorted-array/)

---

---

Here’s a crisp interview-style guide for **K-th Missing Positive Number in a Sorted Array**.

---

## 2) Intuition & step-by-step dry run

### Core idea

For a sorted array of **distinct positive** integers `arr`, define

```
missing(i) = arr[i] - (i + 1)
```

This is the count of positive numbers **from 1 up to arr\[i]** that are missing from the array.
Reason: If nothing were missing, the i-th index (0-based) would hold `(i+1)`; the surplus `arr[i] - (i+1)` are exactly the numbers that got skipped.

We want the smallest index `idx` such that `missing(idx) >= k`. Then:

* The answer lies **before or at** `arr[idx]`.
* Exactly `idx` numbers from `1..arr[idx]-1` are present, so the k-th missing number is:

```
answer = k + idx                  (equivalently: arr[idx-1] + (k - missing(idx-1)))
```

If `missing(n-1) < k` (where `n=len(arr)`), the answer is **beyond** the last element:

```
answer = arr[n-1] + (k - missing(n-1))
```

### Dry run

`arr = [2, 3, 4, 7, 11], k = 5`

Compute `missing(i)`:

* `i=0`: `2 - (0+1) = 1`
* `i=1`: `3 - (1+1) = 1`
* `i=2`: `4 - (2+1) = 1`
* `i=3`: `7 - (3+1) = 3`
* `i=4`: `11 - (4+1) = 6`

We need first `i` with `missing(i) ≥ 5` → `i = 4` (since `3 < 5 ≤ 6`).
Answer = `k + idx = 5 + 4 = 9`. ✅

---

## 3) Python solutions (two ways)

### A) Optimal (binary search) — **O(log n)** time, **O(1)** space

```python
class Solution:
    def kthMissing(self, arr, k):
        """
        Binary search for the smallest index idx with missing(idx) >= k,
        where missing(i) = arr[i] - (i + 1).

        Time:  O(log n)
        Space: O(1)
        """
        n = len(arr)
        # Total missing up to the last element
        total_missing = arr[-1] - n
        if total_missing < k:
            # k-th missing is beyond the last array element
            return arr[-1] + (k - total_missing)

        # Find first index with missing(idx) >= k (lower_bound)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] - (mid + 1) >= k:
                hi = mid
            else:
                lo = mid + 1

        # lo is that first index; answer is k + lo (proof in explanation)
        return k + lo
```

### B) Simple scan (two-pointer “count missing” walk) — **O(n + k)** time, **O(1)** space

```python
class SolutionLinear:
    def kthMissing(self, arr, k):
        """
        Walk from 1 upward, skipping elements of arr.
        Good for moderate k; worst-case O(n + k).

        Time:  O(n + k)
        Space: O(1)
        """
        i, cur = 0, 1
        n = len(arr)
        while True:
            if i < n and arr[i] == cur:
                i += 1
            else:
                k -= 1
                if k == 0:
                    return cur
            cur += 1
```

(For large gaps / k, prefer the binary-search solution.)

---

## 4) Interview Q\&A (high-yield)

**Q1. Why is `missing(i) = arr[i] - (i+1)`?**
If no numbers were missing, positions would be `1,2,3,...` so index `i` should have `(i+1)`. The difference to `arr[i]` counts how many were skipped up to there.

**Q2. How do you handle the case when k exceeds all missing inside the array range?**
Compute `total_missing = arr[-1] - n`. If `total_missing < k`, the answer is after the last element: `arr[-1] + (k - total_missing)`.

**Q3. Edge cases?**

* If the first element is greater than 1, missing numbers start at `1`. The binary method still works and will return `k` when `idx=0`.
* Distinct, positive, sorted inputs are assumed. If not sorted, sort first (but then time is `O(n log n)`).

**Q4. Why is the answer `k + idx` after binary search?**
Among numbers `≤ answer`, exactly `idx` are present in `arr` (those before `arr[idx]`). To get `k` numbers **missing**, push the target right by those `idx` present numbers → `answer = k + idx`.

**Q5. Complexity comparison?**

* Binary search: **O(log n)** time, **O(1)** space — preferred.
* Linear walk: **O(n + k)** — fine if `k` is small / gaps small.


---

---

Here you go — a complete, runnable script that includes:

* The **optimal binary-search** solution (O(log n), O(1))
* A **simple linear walk** (O(n + k), O(1)) for comparison
* **Inline time measurements** using `timeit`
* **Sample inputs & printed outputs** in `main()`

---

```python
from typing import List
import timeit
import random

# ============================================================
#  K-th Missing Positive Number in a Sorted Array
#  - arr is sorted, distinct, positive integers
# ============================================================

class Solution:
    def kthMissing(self, arr: List[int], k: int) -> int:
        """
        Optimal binary-search approach.
        missing(i) = how many positives are missing up to arr[i]
                   = arr[i] - (i + 1)

        If total_missing (up to the last element) < k,
        the k-th missing lies beyond the array.

        Time:  O(log n)  (binary search over indices)
        Space: O(1)
        """
        n = len(arr)
        # Total missing up to arr[n-1]
        total_missing = arr[-1] - n  # O(1)

        if total_missing < k:
            # The answer is beyond arr[-1]:
            # We still need (k - total_missing) numbers after arr[-1].
            return arr[-1] + (k - total_missing)

        # Binary search: first index idx with missing(idx) >= k
        lo, hi = 0, n - 1            # O(1)
        while lo < hi:               # O(log n) iterations
            mid = (lo + hi) // 2
            # missing(mid) = arr[mid] - (mid + 1)
            if arr[mid] - (mid + 1) >= k:
                hi = mid
            else:
                lo = mid + 1

        # lo is the first position with missing(lo) >= k.
        # Among numbers <= answer, exactly 'lo' are present in arr.
        # To get k missing, shift by lo: answer = k + lo
        return k + lo


class SolutionLinear:
    def kthMissing(self, arr: List[int], k: int) -> int:
        """
        Linear walk from positive 'cur' upward, skipping arr elements.
        Each number not in arr consumes one from k until k==0.

        Time:  O(n + k)     (we may step through extra positives)
        Space: O(1)
        """
        i, cur = 0, 1
        n = len(arr)
        # Walk until we've consumed k missing numbers
        while True:                   # Worst case O(n + k)
            if i < n and arr[i] == cur:
                i += 1                # O(1)
            else:
                k -= 1                # Found one missing value
                if k == 0:
                    return cur
            cur += 1                  # Move to next positive


# ------------------------------------------------------------
# Demo / main with timings & printed outputs
# ------------------------------------------------------------
def main():
    opt = Solution()
    lin = SolutionLinear()

    print("=== K-th Missing Positive Number — Demo & Timing ===")

    # --------- Examples from prompt ---------
    examples = [
        # (arr, k, expected)
        ([2, 3, 4, 7, 11], 5, 9),
        ([1, 2, 3],        2, 5),
        ([3, 5, 9, 10, 11, 12], 2, 2),
    ]

    print("\n-- Examples --")
    for arr, k, exp in examples:
        # Binary search timing
        t0 = timeit.default_timer()
        out_bs = opt.kthMissing(arr, k)
        t1 = timeit.default_timer()
        # Linear walk timing
        t2 = timeit.default_timer()
        out_ln = lin.kthMissing(arr, k)
        t3 = timeit.default_timer()

        print(f"arr={arr}, k={k}")
        print(f"  Binary: {out_bs} (exp {exp})  time={(t1 - t0):.6f}s")
        print(f"  Linear: {out_ln} (exp {exp})  time={(t3 - t2):.6f}s")
        print("-" * 80)

    # --------- Randomized cross-checks ---------
    print("\n-- Random cross-checks (small/medium) --")
    random.seed(7)
    for _ in range(5):
        # build a sorted distinct positive array
        n  = random.randint(5, 20)
        up = random.randint(n + 3, n + 15)     # some extra gaps
        arr = sorted(random.sample(range(1, up + 1), n))
        k   = random.randint(1, 10)

        out_bs = opt.kthMissing(arr, k)
        out_ln = lin.kthMissing(arr, k)
        verdict = "OK" if out_bs == out_ln else "MISMATCH"
        print(f"arr={arr}, k={k} -> Binary={out_bs}, Linear={out_ln}  [{verdict}]")

    # --------- Larger benchmark (shows O(log n) vs O(n+k)) ---------
    print("\n-- Larger benchmark --")
    n = 100_000
    # Create a nearly full 1..(n + gap) with some deletions to create gaps
    full_end = n + 50_000
    # choose n distinct numbers to be present
    arr = sorted(random.sample(range(1, full_end + 1), n))
    k   = 40_000  # fairly large k

    t0 = timeit.default_timer()
    res_bs = opt.kthMissing(arr, k)
    t1 = timeit.default_timer()
    print(f"Binary: result={res_bs}, time={(t1 - t0):.6f}s")

    t2 = timeit.default_timer()
    res_ln = lin.kthMissing(arr, k)
    t3 = timeit.default_timer()
    print(f"Linear: result={res_ln}, time={(t3 - t2):.6f}s")


if __name__ == "__main__":
    start_all = timeit.default_timer()
    main()
    end_all = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end_all - start_all):.6f} seconds")
```

---

## 6) Real-World Use Cases (high-impact, concise)

* **Telemetry stream gap analysis:** Given a sorted list of consumed message IDs, find the K-th missing ID for backfill or replay.
* **Inventory/serial audits:** With recorded serial numbers, locate the K-th missing serial for reconciliation.
* **API rate window checks:** Determine the K-th unhit request sequence index inside a rolling window for diagnostics.
* **Data migration verification:** When verifying monotonic keys post-migration, identify K-th gap to target validation or repair steps.

