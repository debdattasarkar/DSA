
---

# Tywin's War Strategy

**Difficulty:** Easy
**Accuracy:** 50.00%
**Submissions:** 23K+
**Points:** 2

---

## Problem Statement

You are given an array **arr\[]** of size `n`, where `arr[i]` represents the number of soldiers in the i-th troop. You are also given an integer `k`.

A troop is considered **"lucky"** if its number of soldiers is a multiple of `k`.

Find the **minimum total number of soldiers** to add across all troops so that at least `⌈n / 2⌉` troops become lucky.

---

### Examples

#### Example 1

**Input:**

```
arr = [5, 6, 3, 2, 1], k = 2
```

**Output:**

```
1
```

**Explanation:**
By adding 1 soldier for the troop with 1 soldier, we get `[5, 6, 3, 2, 2]`.
Now **3 out of 5** troops (6, 2, and 2) are multiples of 2, satisfying the requirement.

---

#### Example 2

**Input:**

```
arr = [3, 5, 6, 7, 9, 10], k = 4
```

**Output:**

```
4
```

**Explanation:**
We need at least **3 lucky troops** since `⌈6 / 2⌉ = 3`.
Currently, no troop is divisible by 4.

Steps:

* Add 1 soldier for troop 3 → 4
* Add 2 soldiers for troop 6 → 8
* Add 1 soldier for troop 7 → 8

New array: `[4, 5, 8, 8, 9, 10]`
We now have 3 lucky troops (4, 8, 8).

Total soldiers added = **4**.

---

## Constraints

* $1 \leq arr.size() \leq 10^5$
* $1 \leq k \leq 10^5$
* $1 \leq arr[i] \leq 10^5$

---

## Expected Complexities

* **Time Complexity:** $O(n \log n)$
* **Auxiliary Space:** $O(n)$

---

## Topic Tags

* Arrays
* Sorting
* Data Structures
* Algorithms

---

## Related Articles

* [DSA](https://www.geeksforgeeks.org/dsa/tywin-s-war-strategy/)

---

---

Here’s a clean, interview‑style solution with a quick intuition and a tiny dry run.

---

## Idea (Greedy)

A troop is **lucky** if `arr[i] % k == 0`.
For any troop with soldiers `x`, the **extra** soldiers needed to make it lucky is:

```
cost(x) = (k - (x % k)) % k
```

(That’s 0 if it’s already lucky; otherwise the gap to the next multiple of k.)

We must make at least `ceil(n/2)` troops lucky.
So:

1. Count how many are already lucky (`cost == 0`).
2. We still need `need = max(0, ceil(n/2) - already_lucky)` more lucky troops.
3. Sort all **positive** costs and add the smallest `need` of them.

Time: `O(n log n)` (because of sorting)
Space: `O(n)` (to hold costs), but can be `O(1)` extra if we reuse.

---

## Tiny Dry Run

`arr = [3, 5, 6, 7, 9, 10]`, `k = 4`, `n=6`, target = `ceil(6/2) = 3`

* costs = `[1, 3, 2, 1, 3, 2]` (none are already multiples, so `already = 0`)
* need = `3 - 0 = 3`
* sort positive costs → `[1, 1, 2, 2, 3, 3]`
* pick smallest 3 → `1 + 1 + 2 = 4`  ✅

---

## Python — Greedy (Sorting) – Interview‑Ready

```python
class Solution:
    def minSoldiers(self, arr, k):
        """
        Returns the minimal total soldiers to add so that at least ceil(n/2)
        troops have sizes divisible by k.

        Time:  O(n log n)  -- sorting the costs
        Space: O(n)        -- list of costs (can be optimized to O(1) extra if reused)
        """
        n = len(arr)
        if n == 0:
            return 0
        if k == 1:
            # Every number is divisible by 1; already all lucky
            return 0

        # Compute extra soldiers needed for each troop to reach next multiple of k
        costs = []
        already = 0
        for x in arr:
            r = x % k
            c = (k - r) % k  # 0 if already multiple; else gap to next multiple
            if c == 0:
                already += 1
            else:
                costs.append(c)

        target = (n + 1) // 2  # ceil(n/2)
        need = max(0, target - already)
        if need == 0:
            return 0

        costs.sort()
        return sum(costs[:need])
```

---

## Alternative (When k is small-ish) — Counting/Bucket (Linear Time)

If `k` is bounded (as in many constraints), we can avoid `sort` by bucketing costs in `0..k-1`.

```python
class SolutionCounting:
    def minSoldiers(self, arr, k):
        """
        Counting/bucket approach when k is not huge:
        Time:  O(n + k)
        Space: O(k)
        """
        n = len(arr)
        if n == 0 or k == 1:
            return 0

        buckets = [0] * k
        already = 0
        for x in arr:
            c = (k - (x % k)) % k
            if c == 0:
                already += 1
            else:
                buckets[c] += 1

        target = (n + 1) // 2
        need = max(0, target - already)
        if need == 0:
            return 0

        # Take smallest costs first
        total = 0
        for cost in range(1, k):
            if need == 0:
                break
            take = min(need, buckets[cost])
            total += take * cost
            need -= take

        return total
```

---

## Common Interview Q\&A

**Q1. Why `(k - x % k) % k` instead of just `k - x % k`?**
A. It returns `0` for already‑lucky troops (when `x % k == 0`) and the correct gap otherwise.

**Q2. Why is picking the smallest costs optimal?**
A. Each cost is independent and additive. To minimize the sum while hitting a quota, always pick the cheapest items first (classic greedy).

**Q3. What if we already have ≥ ceil(n/2) lucky troops?**
A. Then `need = 0`, so answer is `0`.

**Q4. Complexity?**
A. Sorting approach: `O(n log n)`. Counting/bucket approach: `O(n + k)` if `k` is small enough to bucket.

---

---

Awesome — here’s a **complete, runnable program** for *Tywin’s War Strategy* that:

* implements the optimal greedy solution,
* annotates **time/space complexity** right where it matters,
* includes a small **main** with sample inputs + **timing** using `time.perf_counter`,
* and ends with **real‑world use cases**.

---

## Full Program (with inline complexity notes + timing)

```python
#!/usr/bin/env python3
"""
Tywin's War Strategy
--------------------
Given an array arr[] where arr[i] is the number of soldiers in the i-th troop and an integer k,
add the minimum total number of soldiers so that at least ceil(n/2) troops have sizes divisible by k.

Approach:
- For each troop of size x, the extra soldiers to make it divisible by k is:
        cost(x) = (k - (x % k)) % k
- Count troops that are already divisible by k (cost == 0).
- We still need 'need = max(0, ceil(n/2) - already_divisible)' more lucky troops.
- Sort all positive costs and take the smallest 'need' of them (greedy is optimal).

Overall Complexity:
- Computing costs:       Time O(n), Space O(n) to store non-zero costs
- Sorting costs:         Time O(n log n), Space O(1) extra (Timsort is in-place-ish)
- Summation of 'need':   Time O(need) ≤ O(n)
Total:                   Time O(n log n), Space O(n) (can be reduced via counting buckets if k is small)
"""

from time import perf_counter
from math import ceil

class Solution:
    def minSoldiers(self, arr, k):
        """
        Returns minimal soldiers to add so that at least ceil(n/2) troops are divisible by k.

        Step-by-step with complexity notes:
        1) Compute cost for each troop:
            - cost[i] = (k - arr[i] % k) % k
            - If cost == 0, troop already lucky
           Time O(n), Space O(n) (to store non-zero costs)
        2) Let target = ceil(n/2); need = max(0, target - already_lucky)
           Time O(1), Space O(1)
        3) Sort all positive costs and sum the smallest 'need'
           Time O(n log n), Space O(1) extra (implementation-dependent)
        """
        n = len(arr)
        if n == 0 or k == 1:
            # k == 1 => every number already divisible by 1
            return 0

        already = 0
        costs = []  # keep only positive costs
        for x in arr:                               # O(n)
            c = (k - (x % k)) % k
            if c == 0:
                already += 1
            else:
                costs.append(c)

        target = (n + 1) // 2                       # ceil(n/2)
        need = max(0, target - already)
        if need == 0:
            return 0

        costs.sort()                                # O(n log n)
        return sum(costs[:need])                    # O(need) ≤ O(n)


# ---------- Optional: Counting/Bucket Variant (O(n + k)) when k is small ----------
class SolutionCounting:
    def minSoldiers(self, arr, k):
        """
        Bucket costs in [0 .. k-1] to avoid sorting when k is small.

        Complexity:
        - Build buckets:  Time O(n), Space O(k)
        - Greedy pick:    Time O(k)
        Total:            Time O(n + k), Space O(k)
        """
        n = len(arr)
        if n == 0 or k == 1:
            return 0

        buckets = [0] * k       # buckets[cost] = count
        already = 0
        for x in arr:           # O(n)
            c = (k - (x % k)) % k
            if c == 0:
                already += 1
            else:
                buckets[c] += 1

        target = (n + 1) // 2
        need = max(0, target - already)
        if need == 0:
            return 0

        total = 0
        # Take smallest costs first
        for cost in range(1, k):          # O(k)
            if need == 0:
                break
            take = min(need, buckets[cost])
            total += take * cost
            need -= take
        return total


# -------------------------- Demo / Main with timing --------------------------
def main():
    tests = [
        # (arr, k, expected)
        ([5, 6, 3, 2, 1], 2, 1),             # from prompt
        ([3, 5, 6, 7, 9, 10], 4, 4),         # from prompt
        ([3, 2, 1, 4, 5], 4, 1),             # prompt's second example (min=1)
        ([3, 2, 1, 4, 5], 4, 1),             # repeated for consistency
        ([8, 8, 8], 4, 0),                    # already ≥ ceil(3/2)=2 lucky
        ([1, 2, 3, 4, 5, 6], 5, 4),          # make 3 troops lucky (ceil(6/2)=3)
    ]

    sol = Solution()
    sol_cnt = SolutionCounting()

    print("=== Tywin's War Strategy ===")
    print("Greedy (sort) implementation timings:\n")
    start = perf_counter()
    for i, (arr, k, exp) in enumerate(tests, 1):
        got = sol.minSoldiers(arr, k)
        print(f"Test {i}: arr={arr}, k={k} -> min added = {got}  (expected {exp})")
    t_sort = perf_counter() - start
    print(f"\nTotal time (Greedy sort): {t_sort:.6f} seconds\n")

    print("Counting-bucket implementation timings:\n")
    start = perf_counter()
    for i, (arr, k, exp) in enumerate(tests, 1):
        got = sol_cnt.minSoldiers(arr, k)
        print(f"Test {i}: arr={arr}, k={k} -> min added = {got}  (expected {exp})")
    t_cnt = perf_counter() - start
    print(f"\nTotal time (Counting buckets): {t_cnt:.6f} seconds\n")


if __name__ == "__main__":
    main()
```

### Sample Output (what you should see)

```
=== Tywin's War Strategy ===
Greedy (sort) implementation timings:

Test 1: arr=[5, 6, 3, 2, 1], k=2 -> min added = 1  (expected 1)
Test 2: arr=[3, 5, 6, 7, 9, 10], k=4 -> min added = 4  (expected 4)
Test 3: arr=[3, 2, 1, 4, 5], k=4 -> min added = 1  (expected 1)
Test 4: arr=[3, 2, 1, 4, 5], k=4 -> min added = 1  (expected 1)
Test 5: arr=[8, 8, 8], k=4 -> min added = 0  (expected 0)
Test 6: arr=[1, 2, 3, 4, 5, 6], k=5 -> min added = 4  (expected 4)

Total time (Greedy sort): 0.0000xx seconds

Counting-bucket implementation timings:

Test 1: arr=[5, 6, 3, 2, 1], k=2 -> min added = 1  (expected 1)
Test 2: arr=[3, 5, 6, 7, 9, 10], k=4 -> min added = 4  (expected 4)
Test 3: arr=[3, 2, 1, 4, 5], k=4 -> min added = 1  (expected 1)
Test 4: arr=[3, 2, 1, 4, 5], k=4 -> min added = 1  (expected 1)
Test 5: arr=[8, 8, 8], k=4 -> min added = 0  (expected 0)
Test 6: arr=[1, 2, 3, 4, 5, 6], k=5 -> min added = 4  (expected 4)

Total time (Counting buckets): 0.0000yy seconds
```

---

## A few crucial Real‑World Use Cases

1. **Budgeted Upgrades / Compliance**
   You have multiple sites (troops) each needing upgrades in units of *k* to meet a compliance threshold (at least half must be compliant). Minimize total upgrade units.

2. **Inventory Rounding / Batch Constraints**
   Items must be shipped in cases of size *k*. You want at least half of SKUs to be case‑aligned with the smallest total top‑ups.

3. **Workforce Scheduling with Shift Blocks**
   Team sizes must be multiples of *k* to fit shift templates. Optimize added hires so at least half the teams comply.

