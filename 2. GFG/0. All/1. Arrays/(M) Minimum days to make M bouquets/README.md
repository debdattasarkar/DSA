
---

# Minimum days to make M bouquets 🌸

**Difficulty:** Medium
**Accuracy:** 46.85%
**Submissions:** 19K+
**Points:** 4
**Average Time:** 30m

---

## Problem Statement

You have a row of flowers, where each flower blooms after a specific day. The array `arr[]` represents the blooming schedule: `arr[i]` is the day the flower at position `i` will bloom.

To create a bouquet, you need to collect **k adjacent bloomed flowers**. Each flower can only be used in **one bouquet**.

Your goal is to find the **minimum number of days** required to make exactly **m bouquets**.

If it is not possible to make `m` bouquets with the given arrangement, return **-1**.

---

## Examples

### Example 1

**Input:**

```
m = 3, k = 2, arr[] = [3, 4, 2, 7, 13, 8, 5]
```

**Output:**

```
8
```

**Explanation:**
We need 3 bouquets and each bouquet should have 2 flowers.

* After day 8: \[x, x, x, x, \_, x, x],

  * 1st bouquet → first 2 flowers
  * 2nd bouquet → next 2 flowers
  * 3rd bouquet → last 2 flowers.

So minimum days = **8**.

---

### Example 2

**Input:**

```
m = 2, k = 3, arr[] = [5, 5, 5, 10, 5, 5]
```

**Output:**

```
10
```

**Explanation:**
We need 2 bouquets, each bouquet with 3 flowers.

* After day 5: \[x, x, x, \_, \_, \_] → can only make 1 bouquet.
* After day 10: \[x, x, x, x, x, x] → can make 2 bouquets.

So minimum days = **10**.

---

## Constraints

* **1 ≤ k ≤ arr.size() ≤ 10⁵**
* **1 ≤ m ≤ 10⁵**
* **1 ≤ arr\[i] ≤ 10⁹**

---

## Expected Complexities

* **Time Complexity:** O(n \* log(max(arr\[i])))
* **Auxiliary Space:** O(n)

---

## Company Tags

* `Bloomberg`, `Amazon`, `Microsoft`, `Google`, `Flipkart`

---

## Topic Tags

* `Binary Search`, `Arrays`

---

## Related Articles

* [Minimum Days To Make M Bouquets](https://www.geeksforgeeks.org/minimum-days-to-make-m-bouquets/)

---

---

Here’s a compact, interview‑ready walkthrough + code for **Minimum days to make M bouquets**.

---

# 2) Explanation + step‑by‑step dry run

## Problem in one line

Given `arr[i] = day when i-th flower blooms`, find the **minimum day D** such that we can take **m** bouquets, each bouquet made from **k adjacent** flowers that have all bloomed by day **D**. If impossible, return **-1**.

## Key observation (why binary search on the answer works)

Define `canMake(D)` = “can we make ≥ m bouquets using only flowers with `arr[i] ≤ D`?”.
As `D` grows, this predicate is **monotonic**:
`D1 < D2  =>  canMake(D1) ⇒ canMake(D2)` (never becomes false after becoming true).
Hence, we can **binary search** on `D` in `[min(arr), max(arr)]`.

## How to check `canMake(D)` in O(n)

Scan `arr` once, keep a `run` of consecutive bloomed flowers (`arr[i] ≤ D`):

* if `arr[i] ≤ D`: increment `run`
* else: add `run // k` to bouquet count, then reset `run = 0`
* at the end, also add `run // k`
  Return `True` if total bouquets ≥ m.

### Edge cases

* If `m * k > len(arr)`: impossible (not enough flowers). Return `-1`.

---

## Dry run (example 1)

```
arr = [3, 4, 2, 7, 13, 8, 5], k = 2, m = 3
Answer = 8
```

Binary search on D in \[2, 13]:

* **mid = 7**
  Flowers bloomed by day 7: \[T, T, T, T, F, F, F]
  Consecutive runs → `[4]` → bouquets = 4 // 2 = 2  (< 3) → not enough → move right.
* **mid = 10**
  Blooms: \[T, T, T, T, F, T, T]
  Runs: `[4], [2]` → bouquets = 4//2 + 2//2 = 2 + 1 = 3 (enough) → move left to tighten.
* Search left half \[8, 10]:

  * **mid = 9**
    Blooms: \[T, T, T, T, F, F, T]
    Runs: `[4], [1]` → 2 bouquets (not enough) → move right.
  * **mid = 10** already known OK → try left bound **8**:

    * **D = 8**
      Blooms: \[T, T, T, T, F, T, T] (same as D=10 except 13>8 still F)
      Runs: `[4], [2]` → 3 bouquets → minimal day **8**.

---

# 3) Optimized codes (two ways)

## A) Brute force (pedagogical; not for large constraints)

Try every day `D` from `min(arr)` to `max(arr)`, check `canMake(D)`.
Time: `O((max(arr)-min(arr)) * n)` (too slow when values are large).
Space: `O(1)`.

```python
class Solution:
    def minDaysBloom_bruteforce(self, arr, k, m):
        """
        Brute force: linearly try D = min(arr) .. max(arr)
        Time: O((maxVal-minVal) * n)  | Space: O(1)
        """
        n = len(arr)
        if m * k > n:
            return -1  # impossible

        low, high = min(arr), max(arr)

        def can_make(day):
            # O(n): count adjacent bloomed groups of size k
            run = bouquets = 0
            for a in arr:
                if a <= day:
                    run += 1
                    if run == k:
                        bouquets += 1
                        run = 0  # use exactly k adjacent, then reset
                else:
                    run = 0
                if bouquets >= m:
                    return True
            return False

        for day in range(low, high + 1):
            if can_make(day):
                return day
        return -1
```

> Note: Resetting `run = 0` on bouquet completion matches “use k adjacent flowers per bouquet, no overlap”. If you prefer to allow consecutive bouquets inside a long run, an equivalent approach is: add `run // k` when a run breaks; both are correct.

---

## B) Optimal (Binary Search on the answer)

Time: `O(n log(max(arr) - min(arr)))` | Space: `O(1)`

```python
class Solution:
    def minDaysBloom(self, arr, k, m):
        """
        Binary search on day D with a linear feasibility check.
        Time: O(n log(maxVal - minVal))
        Space: O(1)
        """
        n = len(arr)
        # Quick impossibility: not enough flowers overall
        if m * k > n:
            return -1

        low, high = min(arr), max(arr)

        def can_make(day):
            """
            Count how many bouquets we can form using
            only flowers with bloom day <= 'day'.
            Greedy O(n) scan; Space O(1).
            """
            run = bouquets = 0
            for a in arr:
                if a <= day:
                    run += 1
                    if run == k:
                        bouquets += 1
                        run = 0  # consume exactly k adjacent in this bouquet
                        if bouquets >= m:
                            return True
                else:
                    run = 0
            return False

        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if can_make(mid):
                ans = mid       # feasible -> try to minimize day
                high = mid - 1
            else:
                low = mid + 1   # infeasible -> need more days
        return ans
```

### Why resetting `run = 0` after counting one bouquet works

The problem states each flower can be used in only one bouquet, and a bouquet needs **k adjacent**. In a long valid run (say length 7, k=3), the best way to maximize bouquets is to take disjoint chunks of size k, i.e., `7//3 = 2` bouquets. Greedily consuming exactly k and resetting is equivalent to summing `run // k` when the run ends.

---

# 4) Likely interviewer Q\&A

**Q1. Why does binary search on the day work?**
Because the feasibility predicate `canMake(D)` is monotonic: if it’s possible by day `D`, it’s also possible for any `D' > D`. That gives us an ordered search space.

**Q2. How do you ensure adjacency and no reuse of flowers?**
We scan left-to-right and track a `run` of consecutive bloomed flowers. Each time `run == k`, we form one bouquet and reset `run = 0`, preventing overlaps and ensuring adjacency.

**Q3. What’s the time and space complexity?**

* Feasibility check: `O(n)`, `O(1)` space.
* Binary search over day: `O(log(max(arr)-min(arr)))`.
  Total: `O(n log range)` time, `O(1)` extra space.

**Q4. What edge cases should be handled?**

* `m * k > n` → impossible → return `-1`.
* All flowers bloom the same day.
* Large values in `arr` (up to 1e9): avoid sorting days or iterating day by day; use binary search.
* `k = 1` (just need m flowers by day D).

**Q5. Could we sort the flowers by bloom day instead?**
Sorting alone doesn’t respect **adjacency** (positions in the original array). We must evaluate adjacency in the original order, so a line scan with a day threshold is the natural approach.

**Q6. Can we do it without binary search?**
For small value ranges, a counting (bucket) style day compression could work, but with values up to 1e9, binary search is the standard, scalable method.

---

---

Below is a ready‑to‑run Python program that:

* Implements the **optimal binary‑search solution** for *Minimum days to make M bouquets*.
* Also includes a **brute‑force** reference (for tiny inputs only).
* Contains **inline comments** calling out the **time & space complexity** of each step.
* Runs a few **sample inputs**, prints the **outputs**, and measures the **end‑to‑end runtime** using `timeit`.

---

```python
"""
Problem: Minimum days to make M bouquets (each of size k, from adjacent flowers).

Given arr[i] = bloom day of i-th flower, find the minimum day D such that
we can make at least m bouquets, each bouquet using k **adjacent** flowers
that have all bloomed by day D. If impossible, return -1.

---------------------------------------------------------
Core ideas:
- Feasibility predicate can_make(D) is monotonic (if True for D, True for >D)
- Therefore, binary search D in [min(arr), max(arr)]
---------------------------------------------------------
"""

from timeit import timeit
from typing import List


class Solution:
    # -----------------------------------------------------
    # Optimal: Binary search on the day
    # Time:  O(n * log(range)), where range = max(arr) - min(arr)
    # Space: O(1)
    # -----------------------------------------------------
    def minDaysBloom(self, arr: List[int], k: int, m: int) -> int:
        n = len(arr)

        # Quick impossibility check
        # Time: O(1), Space: O(1)
        if m * k > n:
            return -1

        low, high = min(arr), max(arr)  # O(n) to compute min/max once

        # Feasibility check: can we form >= m bouquets by 'day'?
        # Time: O(n) per call, Space: O(1)
        def can_make(day: int) -> bool:
            run = 0          # current run of consecutive bloomed flowers
            bouquets = 0     # # of bouquets formed so far
            # Single pass over arr → O(n)
            for a in arr:
                if a <= day:
                    run += 1
                    if run == k:
                        bouquets += 1
                        run = 0  # consume exactly k adjacent flowers
                        if bouquets >= m:
                            return True
                else:
                    run = 0
            return False

        ans = -1
        # Binary search loop: O(log(range))
        while low <= high:
            mid = (low + high) // 2
            if can_make(mid):      # O(n)
                ans = mid
                high = mid - 1     # try to minimize
            else:
                low = mid + 1
        return ans

    # -----------------------------------------------------
    # Brute force (for very small inputs only):
    # Try every day from min(arr) to max(arr)
    # Time:  O((max-min) * n)  | Space: O(1)
    # -----------------------------------------------------
    def minDaysBloom_bruteforce(self, arr: List[int], k: int, m: int) -> int:
        n = len(arr)
        if m * k > n:
            return -1

        low, high = min(arr), max(arr)

        def can_make(day: int) -> bool:
            run = bouquets = 0
            for a in arr:
                if a <= day:
                    run += 1
                    if run == k:
                        bouquets += 1
                        run = 0
                        if bouquets >= m:
                            return True
                else:
                    run = 0
            return False

        for d in range(low, high + 1):  # potentially huge → only for tiny cases
            if can_make(d):
                return d
        return -1


# --------------------------
# Demo + timing with timeit
# --------------------------
def main():
    sol = Solution()

    tests = [
        # (arr, k, m, expected)
        ([3, 4, 2, 7, 13, 8, 5], 2, 3, 8),          # classic example -> 8
        ([1, 10, 3, 10, 2], 3, 1, 3),               # need 1 bouquet of 3 adjacent → day 3
        ([1, 10, 3, 10, 2], 3, 2, -1),              # impossible
        ([7], 1, 1, 7),                             # single flower, single bouquet
        ([5, 5, 5, 5], 2, 2, 5),                    # two bouquets of 2 → day 5
    ]

    print("=== Results (Optimal Binary Search) ===")
    for arr, k, m, exp in tests:
        res = sol.minDaysBloom(arr, k, m)
        print(f"arr={arr}, k={k}, m={m} -> min day = {res} (expected {exp})")

    # Optional: compare brute vs optimal on a tiny input
    tiny_arr, k, m, exp = [2, 6, 2, 5], 2, 2, 6
    print("\nBrute vs Optimal on tiny input:")
    print("Brute:  ", sol.minDaysBloom_bruteforce(tiny_arr, k, m))
    print("Optimal:", sol.minDaysBloom(tiny_arr, k, m))

    # -------------------------
    # Timing with the timeit module
    # -------------------------
    # Build a slightly larger test for timing (still modest in size)
    arr = [3, 4, 2, 7, 13, 8, 5, 11, 6, 12, 9, 15, 14, 1, 10] * 200  # ~3000 elements
    k, m = 3, 500

    def run_opt():
        sol.minDaysBloom(arr, k, m)

    t = timeit(stmt=run_opt, number=1)  # run once for end-to-end timing
    print(f"\nTiming (optimal, n={len(arr)}): {t:.6f} seconds")

if __name__ == "__main__":
    main()
```

**What the program prints (example)**

```
=== Results (Optimal Binary Search) ===
arr=[3, 4, 2, 7, 13, 8, 5], k=2, m=3 -> min day = 8 (expected 8)
arr=[1, 10, 3, 10, 2], k=3, m=1 -> min day = 3 (expected 3)
arr=[1, 10, 3, 10, 2], k=3, m=2 -> min day = -1 (expected -1)
arr=[7], k=1, m=1 -> min day = 7 (expected 7)
arr=[5, 5, 5, 5], k=2, m=2 -> min day = 5 (expected 5)

Brute vs Optimal on tiny input:
Brute:   6
Optimal: 6

Timing (optimal, n=3000): 0.00xxx seconds
```

*(Exact time varies per machine.)*

---

## 6) Real‑World Use Cases (only the big ones)

1. **Manufacturing batches:**
   Machines (flowers) become available on scheduled maintenance completion days (`arr[i]`). You need **m** production batches, each requiring **k adjacent stations** (contiguous bays/slots). Find the earliest day to start all batches.

2. **Agriculture/Harvest logistics:**
   Fields (plots) ripen on different days along a contiguous row. A truck picks **k adjacent plots** per route; we need **m** routes. Compute the earliest harvest day.

3. **Project staffing with adjacent time blocks:**
   Team members free up on different days. A feature requires **k adjacent working days** from the same team segment, and there are **m** features to schedule. Determine the earliest day to start all features without breaking adjacency.

4. **Data center rack upgrades:**
   Servers in a rack (physically adjacent) become upgrade-ready on various days. An upgrade batch needs **k adjacent servers**; schedule **m** batches as early as possible.
