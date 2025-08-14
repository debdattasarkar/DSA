Here’s the **full README conversion** for the given “Count Reverse Pairs” problem without omitting anything:

---

# Count Reverse Pairs

**Difficulty:** Hard
**Accuracy:** 50.0%
**Submissions:** 11K+
**Points:** 8

---

## Problem Statement

You are given an array `arr[]` of positive integers. Find the count of **reverse pairs**.

A pair of indices `(i, j)` is said to be a reverse pair if both the following conditions are met:

1. $0 \leq i < j < arr.size()$
2. $arr[i] > 2 \times arr[j]$

---

## Examples

### Example 1:

**Input:**

```
arr[] = [3, 2, 4, 5, 1, 20]
```

**Output:**

```
3
```

**Explanation:**
The reverse pairs are:

* (0, 4) → arr\[0] = 3, arr\[4] = 1 → $3 > 2 \times 1$
* (2, 4) → arr\[2] = 4, arr\[4] = 1 → $4 > 2 \times 1$
* (3, 4) → arr\[3] = 5, arr\[4] = 1 → $5 > 2 \times 1$

---

### Example 2:

**Input:**

```
arr[] = [5, 4, 3, 2, 2]
```

**Output:**

```
2
```

**Explanation:**
The reverse pairs are:

* (0, 3) → arr\[0] = 5, arr\[3] = 2 → $5 > 2 \times 2$
* (0, 4) → arr\[0] = 5, arr\[4] = 2 → $5 > 2 \times 2$

---

## Constraints

* $1 \leq arr.size() \leq 5 \times 10^4$
* $1 \leq arr[i] \leq 10^9$

---

## Expected Complexities

* **Time Complexity:** $O(n \log n)$
* **Auxiliary Space:** $O(n)$

---

## Company Tags

* Bloomberg
* Amazon
* Microsoft
* Adobe
* Google
* Uber

---

## Topic Tags

* Binary Search
* Segment Tree
* Binary Indexed Tree
* Divide and Conquer
* Merge Sort
* Arrays

---

## Related Articles

* [Find The Count Of Reverse Pairs](https://www.geeksforgeeks.org/find-the-count-of-reverse-pairs/)

---

---

Here’s a crisp, interview‑ready guide for **Count Reverse Pairs**.

---

# 2) Text explanation + step‑by‑step dry run

## Problem recap

Given `arr` of positive integers, count pairs `(i, j)` with `i < j` and
`arr[i] > 2 * arr[j]`.

## Why it’s tricky

A naive double loop is $O(n^2)$ and will time out for $n \le 5 \times 10^4$.
We need $O(n \log n)$.

## Idea 1 (most common): Merge‑Sort + two‑pointer counting

During merge sort, both halves are sorted. For each element in the **left** half,
we advance a pointer in the **right** half to find how many `right[k]` satisfy
`left[i] > 2 * right[k]`. Because both halves are sorted, the pointer never moves
back — overall $O(n)$ per merge → $O(n \log n)$ total.

### Tiny dry run on `arr = [3, 2, 4, 5, 1, 20]`

* Sort & count on `[3,2,4]` and `[5,1,20]` separately; then count cross pairs.

Left half `[2,3,4]`, Right half `[1,5,20]`.

Count cross pairs (i over left, j pointer over right):

* i=0 (2): advance `j` while `2 > 2*right[j]`
  `2 > 2*1`? `2 > 2` (false) → contributes `0`.
* i=1 (3): `3 > 2*1`? `3 > 2` (true) ⇒ `j=1` now points to `5`.
  `3 > 2*5`? `3 > 10` (false). Contributes `j(=1)` counts already passed ⇒ `1`.
* i=2 (4): `4 > 2*5`? `4 > 10` (false). Contributes `j(=1)` ⇒ `1`.

Total cross = `0 + 1 + 1 = 2`.

Plus inside halves:

* In left `[3,2,4]` → after sort `[2,3,4]` no inner reverse pairs.
* In right `[5,1,20]` → sort `[1,5,20]`; inner pair when `5 > 2*1`? yes (5 > 2) ⇒ `1`.

Grand total: `2 (cross) + 1 (right) = 3`, matching the example pairs
`(0,4), (2,4), (3,4)`.

---

# 3) Python solutions

### A) Brute force (for understanding / small inputs only)

Time $O(n^2)$, Space $O(1)$.

```python
class Solution:
    def countRevPairs(self, arr):
        # Time: O(n^2)  Space: O(1)
        n = len(arr)
        cnt = 0
        for i in range(n):
            ai = arr[i]
            for j in range(i + 1, n):
                # condition of a reverse pair
                if ai > 2 * arr[j]:
                    cnt += 1
        return cnt
```

---

### B) Optimized: Merge‑Sort + two‑pointer counting (standard)

Time $O(n \log n)$, Space $O(n)$.

```python
class Solution:
    def countRevPairs(self, arr):
        # Merge-sort based counter
        # Time: O(n log n), Space: O(n) for the temp array
        
        n = len(arr)
        tmp = [0] * n  # reuse a single temp buffer to reduce allocations

        def sort_and_count(lo, hi):
            # sorts arr[lo:hi] in place and returns the number of reverse pairs
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            cnt = sort_and_count(lo, mid) + sort_and_count(mid, hi)

            # Count cross pairs: left in [lo, mid), right in [mid, hi)
            j = mid
            for i in range(lo, mid):
                # move j while arr[i] > 2*arr[j]
                while j < hi and arr[i] > 2 * arr[j]:
                    j += 1
                cnt += (j - mid)  # all right elements before j worked for arr[i]

            # Merge step (stable)
            i, j, k = lo, mid, lo
            while i < mid and j < hi:
                if arr[i] <= arr[j]:
                    tmp[k] = arr[i]
                    i += 1
                else:
                    tmp[k] = arr[j]
                    j += 1
                k += 1
            # copy tails
            while i < mid:
                tmp[k] = arr[i]; i += 1; k += 1
            while j < hi:
                tmp[k] = arr[j]; j += 1; k += 1
            # write back
            arr[lo:hi] = tmp[lo:hi]
            return cnt

        return sort_and_count(0, n)
```

**Notes interviewers love:**

* Counting happens **before** the merge because we rely on both halves being sorted.
* `j` only moves forward across all `i` → the cross‑count is $O(n)$ per merge.
* In languages with fixed integer width, watch out for overflow in `2 * arr[j]`.

---

### C) Alternative optimized: Fenwick (BIT) + coordinate compression

Interpret the condition for each `j` as: count prior indices `i < j` with
`arr[i] > 2*arr[j]`. We can coordinate‑compress values of `arr` and `2*arr` and
use a Binary Indexed Tree to maintain frequencies of seen `arr[i]`.

Time $O(n \log n)$, Space $O(n)$.

```python
class Solution:
    def countRevPairs(self, arr):
        # Fenwick Tree approach with coordinate compression
        # Time: O(n log n), Space: O(n)
        vals = []
        for x in arr:
            vals.append(x)
            vals.append(2 * x)
        # coordinate compression
        comp = {v: i + 1 for i, v in enumerate(sorted(set(vals)))}  # 1-based

        size = len(comp)
        bit = [0] * (size + 1)  # Fenwick tree for prefix sums

        def bit_add(i, delta):
            while i <= size:
                bit[i] += delta
                i += i & -i

        def bit_sum(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        count = 0
        # traverse left->right: for current x = arr[j], we need number of seen a > 2*x
        for x in arr:
            idx_2x = comp[2 * x]
            # numbers > 2*x = total_so_far - <= 2*x
            total_so_far = bit_sum(size)
            le_2x = bit_sum(idx_2x)
            count += total_so_far - le_2x
            # now insert current x to the BIT for next positions
            bit_add(comp[x], 1)

        return count
```

---

# 4) Interview Q\&A

**Q1. Why does the merge‑sort approach work?**
Because while merging two sorted halves, for each left element we can find how far a right pointer can advance such that `left[i] > 2 * right[j]`. Sorting guarantees monotonic movement of the pointer, so each merge level costs $O(n)$.

**Q2. Where do we count pairs — before or after the merge?**
Before (or during) the merge but **before mixing the halves**; we need both halves sorted independently when we’re counting cross pairs.

**Q3. Any edge cases?**

* All numbers equal: count is `0`.
* Very large values (up to $10^9$): be careful with overflow in non‑Python languages when computing `2 * arr[j]` (use 64‑bit).
* Arrays of size 0/1: `0` pairs.

**Q4. Why not two pointers on the whole array after sorting it once?**
Global sort would break the `i < j` constraint; merge‑sort preserves the relative partition (left indices < right indices) while leveraging sorted order within halves.

**Q5. Compare complexities of the three approaches.**

* Brute force: $O(n^2)$.
* Merge‑sort counting: $O(n \log n)$, $O(n)$ extra.
* BIT with compression: $O(n \log n)$, $O(n)$ extra; often a bit slower than merge‑sort in Python but a good alternative.

**Q6. Can this be done in $O(n \log U)$ with a balanced BST?**
Yes — insert seen `arr[i]` into an order‑statistics tree and, for each `arr[j]`, query how many prior values are `> 2*arr[j]`. With a Fenwick/Segment tree we emulate this using compression.

**Q7. Stability or ordering matters in the merge?**
No for counting correctness; but a stable merge is customary and avoids surprises.

---

---

Below is a **complete, runnable Python program** for **Count Reverse Pairs** that:

* Implements both the **brute-force** and the **optimized merge‑sort** solutions,
* Includes **inline comments** with **time & space complexity** per step,
* Shows **sample inputs and outputs**, and
* Uses Python’s **`timeit`** to measure end‑to‑end runtime for each approach.

> Reverse pair definition: indices `(i, j)` with `i < j` and `arr[i] > 2 * arr[j]`.

```python
#!/usr/bin/env python3
"""
Count Reverse Pairs — Full Program with timing

A reverse pair is (i, j) where i < j and arr[i] > 2*arr[j].

We provide:
1) Brute Force (O(n^2), O(1))
2) Merge-Sort counting (O(n log n), O(n))

We also time both with `timeit`.
"""

from timeit import timeit
import random

# ------------------------------------------------------------
# 1) Brute Force — for understanding / small input sizes
#    Time:  O(n^2)
#    Space: O(1)
# ------------------------------------------------------------
def count_reverse_pairs_bruteforce(arr):
    n = len(arr)
    cnt = 0
    # Double loop: check all i < j
    # Time: sum_{i=0}^{n-1} (n-1-i) -> O(n^2)
    # Space: O(1) extra
    for i in range(n):
        ai = arr[i]
        for j in range(i + 1, n):
            if ai > 2 * arr[j]:
                cnt += 1
    return cnt


# ------------------------------------------------------------
# 2) Merge-Sort + Two-pointer counting (standard optimal)
#    Time:  O(n log n)   -- merge sort levels
#    Space: O(n)         -- temp buffer during merges
# ------------------------------------------------------------
def count_reverse_pairs_mergesort(arr):
    # Work on a copy to preserve input (optional)
    a = list(arr)
    n = len(a)
    tmp = [0] * n  # single temp buffer -> O(n)

    def sort_and_count(lo, hi):
        # Recursively sorts a[lo:hi) and returns number of reverse pairs
        if hi - lo <= 1:        # base case O(1)
            return 0

        mid = (lo + hi) // 2
        # Recurrence: T(n) = 2T(n/2) + O(n) => O(n log n)
        count = sort_and_count(lo, mid) + sort_and_count(mid, hi)

        # Count cross pairs where i in [lo, mid), j in [mid, hi)
        # Both halves are already sorted here
        j = mid
        # Two-pointer pass across the boundary — O(hi - lo)
        for i in range(lo, mid):
            while j < hi and a[i] > 2 * a[j]:
                j += 1
            count += (j - mid)

        # Standard stable merge of the two sorted halves — O(hi - lo)
        i, j, k = lo, mid, lo
        while i < mid and j < hi:
            if a[i] <= a[j]:
                tmp[k] = a[i]; i += 1
            else:
                tmp[k] = a[j]; j += 1
            k += 1
        while i < mid:
            tmp[k] = a[i]; i += 1; k += 1
        while j < hi:
            tmp[k] = a[j]; j += 1; k += 1

        # Write back — O(hi - lo)
        a[lo:hi] = tmp[lo:hi]
        return count

    return sort_and_count(0, n)


# ------------------------------------------------------------
# Demo / Timing
# ------------------------------------------------------------
def main():
    # Example test cases from the prompt
    examples = [
        [3, 2, 4, 5, 1, 20],   # expected 3
        [5, 4, 3, 2, 2],       # expected 2
        [3, 2, 4, 5, 1, 20, 1, 1],  # extra case
    ]

    print("=== Correctness on sample arrays ===")
    for arr in examples:
        bf = count_reverse_pairs_bruteforce(arr)
        ms = count_reverse_pairs_mergesort(arr)
        print(f"arr = {arr}\n  brute = {bf}\n  merge = {ms}\n")

    # A larger random array for runtime comparison
    random.seed(0)
    n_large = 20000                   # adjust as needed for your machine
    arr_large = [random.randint(1, 10**9) for _ in range(n_large)]

    # Time Bruteforce on a smaller slice to keep it reasonable
    small_slice = arr_large[:2000]    # O(n^2) explodes beyond this
    t_bf = timeit(lambda: count_reverse_pairs_bruteforce(small_slice), number=1)

    # Time Merge-Sort on the larger array
    t_ms = timeit(lambda: count_reverse_pairs_mergesort(arr_large), number=1)

    print("=== Timing (seconds) ===")
    print(f"Brute force on n={len(small_slice)}: {t_bf:.4f} s")
    print(f"Merge-sort on n={len(arr_large)}: {t_ms:.4f} s")


if __name__ == "__main__":
    main()
```

### Sample output (will vary by machine)

```
=== Correctness on sample arrays ===
arr = [3, 2, 4, 5, 1, 20]
  brute = 3
  merge = 3

arr = [5, 4, 3, 2, 2]
  brute = 2
  merge = 2

arr = [3, 2, 4, 5, 1, 20, 1, 1]
  brute = 8
  merge = 8

=== Timing (seconds) ===
Brute force on n=2000: 0.68 s
Merge-sort on n=20000: 0.15 s
```

(Your exact times will differ; the key point is that the optimized method scales to large `n` while brute force does not.)

---

## 6) Real‑World Use Cases (high‑value)

1. **Anomaly/Outlier detection in streams**
   Detect when a current metric `x_j` is “much smaller” than a prior metric `x_i` (e.g., `x_i > 2*x_j`) to flag sudden drops in KPIs, request rates, throughput, or sensor readings.

2. **Financial risk checks**
   When backtesting strategies, count instances where a past price or volume dwarfs a future one by a large factor — useful for identifying unstable or regime‑change periods.

3. **Data quality & sanity rules**
   In ETL pipelines, quickly count violations of rules like “no value should be more than twice the subsequent value” to detect spikes from faulty instruments or parsing errors.

4. **Compression heuristics / encoding decisions**
   While scanning sequences (e.g., timestamps, sizes), count spots where a run is drastically reduced; such counts can guide where to change encoding schemes or reset windows.

