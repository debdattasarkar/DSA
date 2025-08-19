# Farthest Smaller Right

**Difficulty:** Medium
**Accuracy:** 50.08%
**Submissions:** 13K+
**Points:** 4

---

You are given an array `arr[]`. For each element at index `i` (0‑based indexing), find the **farthest index `j` to the right** (`i.e., j > i`) such that `arr[j] < arr[i]`.
If no such index exists for a given position, return `-1` for that index.
Return the resulting array of answers.

---

## Examples

### Example 1

**Input:** `arr[] = [2, 5, 1, 3, 2]`
**Output:** `[2, 4, -1, 4, -1]`
**Explanation:**

* `arr[0] = 2`: Farthest smaller element to the right is `arr[2] = 1`.
* `arr[1] = 5`: Farthest smaller element to the right is `arr[4] = 2`.
* `arr[2] = 1`: No smaller element to the right → `-1`.
* `arr[3] = 3`: Farthest smaller element to the right is `arr[4] = 2`.
* `arr[4] = 2`: No elements to the right → `-1`.

### Example 2

**Input:** `arr[] = [2, 3, 5, 4, 1]`
**Output:** `[4, 4, 4, 4, -1]`
**Explanation:** `arr[4]` is the farthest smallest element to the right for `arr[0]`, `arr[1]`, `arr[2]`, and `arr[3]`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `1 ≤ arr[i] ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(n)`

---

## Topic Tags

`Binary Search`, `Arrays`, `Data Structures`, `Algorithms`

---

## Related Articles

* [*Find The Farthest Smaller Number In The Right Side*](https://www.geeksforgeeks.org/find-the-farthest-smaller-number-in-the-right-side/)

---

---

Here’s a crisp “interview‑ready” package for the problem.

---

## 2) Explanation + step‑by‑step dry run

We need, for each index `i`, the **farthest** (largest) index `j > i` such that `arr[j] < arr[i]`.
A direct scan per `i` is `O(n²)`. We can do better by observing:

* Define `smin[i] = min(arr[i], arr[i+1], …, arr[n-1])` (suffix minimum).
* `smin` is **non‑increasing** as `i` grows.
* For a fixed `i`, if we look at positions `pos > i`:

  * `smin[pos] < arr[i]` means **there exists** an index `t ∈ [pos..n-1]` with `arr[t] < arr[i]`.
  * The **largest** `pos` with `smin[pos] < arr[i]` is exactly the **farthest** index `t` satisfying `arr[t] < arr[i]`.
    (If there were a smaller value after `t`, then `t` wouldn’t be the farthest.)

So for each `i`, we can **binary‑search** the largest `pos ∈ [i+1..n-1]` with `smin[pos] < arr[i]`.
This gives `O(n log n)` overall.

### Dry run (Example)

`arr = [2, 5, 1, 3, 2]`

Compute suffix minima:

```
smin[4]=2
smin[3]=min(3,2)=2
smin[2]=min(1,2)=1
smin[1]=min(5,1)=1
smin[0]=min(2,1)=1
=> smin = [1, 1, 1, 2, 2]
```

Now per index:

* `i=0` (`arr[i]=2`): search in `[1..4]` largest `pos` with `smin[pos]<2`.
  `smin=[1,1,2,2]` → largest `pos=2`. Answer `2`.
* `i=1` (`5`): search in `[2..4]` for `smin[pos]<5`.
  Always true up to `pos=4`. Answer `4`.
* `i=2` (`1`): search in `[3..4]` for `<1`. None. `-1`.
* `i=3` (`3`): search in `[4..4]` for `<3`. `smin[4]=2` → yes. Answer `4`.
* `i=4`: last index → `-1`.

Result: `[2, 4, -1, 4, -1]`.

---

## 3) Python solutions (with interview‑style inline comments)

### A) Brute force (clear but slow) — `O(n²)` time, `O(1)` extra space

```python
class Solution:
    def farMin(self, arr):
        n = len(arr)
        ans = [-1] * n
        # For each i, scan from the end to i+1 and pick first smaller -> farthest
        for i in range(n - 1):
            for j in range(n - 1, i, -1):                # O(n) per i
                if arr[j] < arr[i]:
                    ans[i] = j                            # farthest found
                    break
        # ans[n-1] stays -1
        return ans
```

### B) Optimized (expected) — Suffix minima + binary search, `O(n log n)` time, `O(n)` space

```python
class Solution:
    def farMin(self, arr):
        n = len(arr)
        if n == 0:
            return []
        
        # 1) Build suffix minima: smin[i] = min(arr[i..n-1])
        #    Time: O(n), Space: O(n)
        smin = [0] * n
        smin[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            smin[i] = arr[i] if arr[i] < smin[i + 1] else smin[i + 1]
        
        # 2) For each i, binary-search largest pos in (i..n-1] with smin[pos] < arr[i]
        #    Time: O(n log n)
        ans = [-1] * n
        for i in range(n - 1):                 # last index remains -1
            lo, hi = i + 1, n - 1
            far = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if smin[mid] < arr[i]:
                    far = mid                  # candidate farthest so far
                    lo = mid + 1               # try to go even farther right
                else:
                    hi = mid - 1
            ans[i] = far
        
        return ans
```

> Why this works: `smin` is non‑increasing, so we can binary‑search.
> The largest `pos` with `smin[pos] < arr[i]` equals the **farthest** index `j` where `arr[j] < arr[i]`.

---

## 4) Likely interviewer Q\&A

**Q1. Why does binary search on the suffix minima give the *index* of the farthest smaller element, not just a proof that one exists?**
**A.** Let `t` be the farthest index with `arr[t] < arr[i]`. For any `pos > t`, no element in `arr[pos..]` is `< arr[i]`, hence `smin[pos] ≥ arr[i]`. For `pos = t`, `smin[t] = min(arr[t..]) = arr[t] < arr[i]`. So the **largest** `pos` with `smin[pos] < arr[i]` is exactly `t`.

**Q2. Why is `smin` non‑increasing?**
**A.** Because each suffix is a subset of the previous one: `min(arr[i..]) ≤ min(arr[i+1..])`.

**Q3. Edge cases?**

* Last index always `-1`.
* Strict “less than” (`<`) comparison is important; using `<=` changes answers.
* All increasing array → answers `[-1,…,-1]`.
* All decreasing array → answers are just the last index `n-1` for all but last.

**Q4. Can we do `O(n)`?**
**A.** With this exact “farthest smaller” requirement, `O(n log n)` via binary search on a monotone array is the standard clean solution (and matches typical expected complexity). A true `O(n)` approach tends to be trickier and is not commonly required in interviews for this task.

**Q5. Space/Time trade‑offs?**
**A.** Brute force uses `O(1)` extra space but `O(n²)` time. The optimized method uses `O(n)` extra space for `smin` to get `O(n log n)` time.

---

---

Awesome — here’s a **complete, runnable program** for *Farthest Smaller Right* that:

* implements both **brute‑force** (`O(n²)`) and **optimized** (`O(n log n)`) solutions,
* contains **inline time/space complexity notes at every logical step**,
* demonstrates with **sample input + printed output**, and
* **times** the two implementations using Python’s `timeit`.

---

### Full Program (copy–paste and run)

```python
#!/usr/bin/env python3
"""
Problem: For each index i in arr, find the farthest index j > i with arr[j] < arr[i],
         or -1 if no such j exists.

This script includes:
  • Brute-force O(n^2) solution
  • Optimized O(n log n) solution using suffix minima + binary search
  • A simple main() with sample inputs/outputs
  • timeit-based benchmarking

Python 3.8+
"""

from timeit import timeit
from random import randint, seed


class Solution:
    # ---------------------------------------------------------------
    # A) Brute-force: O(n^2) time, O(1) extra space
    # ---------------------------------------------------------------
    def farMin_bruteforce(self, arr):
        """
        For each i (0..n-2), scan j from n-1 down to i+1 and pick first j
        with arr[j] < arr[i]. If none, answer is -1.

        Time  : O(n^2)  -- nested loops (worst case scans almost all j for many i)
        Space : O(1)    -- output list aside (not counted as extra)
        """
        n = len(arr)
        ans = [-1] * n                                # O(n) to allocate output
        for i in range(n - 1):                        # O(n) iterations
            for j in range(n - 1, i, -1):            # O(n) per i (worst case)
                if arr[j] < arr[i]:
                    ans[i] = j                       # farthest found (first from right)
                    break
        # ans[n-1] remains -1
        return ans

    # ---------------------------------------------------------------
    # B) Optimized: suffix minima + binary search
    #     • Build smin[i] = min(arr[i..n-1])        -> O(n)
    #     • For each i, binary-search largest pos   -> O(log n)
    #       with smin[pos] < arr[i] on [i+1..n-1]
    #   Overall: O(n log n) time, O(n) space
    # ---------------------------------------------------------------
    def farMin(self, arr):
        """
        Returns list of farthest indices (or -1) to the right with smaller value.

        Time  : O(n log n)
          - Build suffix minima in one pass: O(n)
          - Binary-search per index: O(log n) * n

        Space : O(n)   (for the suffix minima array)
        """
        n = len(arr)
        if n == 0:
            return []

        # ---- Step 1: Build suffix minimum array smin ----
        # smin[i] = min(arr[i], arr[i+1], ..., arr[n-1])
        # Time: O(n), Space: O(n)
        smin = [0] * n
        smin[-1] = arr[-1]
        for i in range(n - 2, -1, -1):                           # O(n)
            # smin is non-increasing; compute in one backward pass
            smin[i] = arr[i] if arr[i] < smin[i + 1] else smin[i + 1]

        # ---- Step 2: For each i, binary search farthest pos > i with smin[pos] < arr[i] ----
        # Time: O(n log n)
        ans = [-1] * n
        for i in range(n - 1):                                    # O(n)
            lo, hi = i + 1, n - 1
            far = -1
            # Binary search on monotone predicate: smin[mid] < arr[i]
            while lo <= hi:                                       # O(log n)
                mid = (lo + hi) // 2
                if smin[mid] < arr[i]:
                    far = mid            # candidate farther position
                    lo = mid + 1         # try to extend farther right
                else:
                    hi = mid - 1         # must move left
            ans[i] = far
        # ans[-1] stays -1
        return ans


# --------------------------------------------------------------------
# Demo + Benchmark
# --------------------------------------------------------------------
def main():
    sol = Solution()

    # ---------- Sample Input 1 ----------
    arr1 = [2, 5, 1, 3, 2]
    print("Input 1 :", arr1)
    print("Brute    :", sol.farMin_bruteforce(arr1))   # Expected: [2, 4, -1, 4, -1]
    print("Optimized:", sol.farMin(arr1))              # Expected: [2, 4, -1, 4, -1]
    print()

    # ---------- Sample Input 2 ----------
    arr2 = [2, 3, 5, 4, 1]
    print("Input 2 :", arr2)
    print("Brute    :", sol.farMin_bruteforce(arr2))   # Expected: [4, 4, 4, 4, -1]
    print("Optimized:", sol.farMin(arr2))              # Expected: [4, 4, 4, 4, -1]
    print()

    # ---------- Quick timing with timeit ----------
    # NOTE: Values will be printed when you RUN this script.
    seed(0)
    n = 20_000  # adjust to taste; keep modest if running on slow machines
    big = [randint(1, 10**9) for _ in range(n)]

    setup_code = (
        "from __main__ import Solution, big\n"
        "sol = Solution()"
    )

    t_brute = timeit("sol.farMin_bruteforce(big[:2000])", setup=setup_code, number=1)
    # (Brute force limited to 2k for time sanity)

    t_opt = timeit("sol.farMin(big)", setup=setup_code, number=1)

    print(f"Timing (approx, one run each):")
    print(f"  Brute-force on 2,000 items : {t_brute:.4f} sec")
    print(f"  Optimized  on {n:,} items  : {t_opt:.4f} sec")


if __name__ == "__main__":
    main()
```

**What the program prints for the samples**

```
Input 1 : [2, 5, 1, 3, 2]
Brute    : [2, 4, -1, 4, -1]
Optimized: [2, 4, -1, 4, -1]

Input 2 : [2, 3, 5, 4, 1]
Brute    : [4, 4, 4, 4, -1]
Optimized: [4, 4, 4, 4, -1]

Timing (approx, one run each):
  Brute-force on 2,000 items : <printed by your machine>
  Optimized  on 20,000 items : <printed by your machine>
```

> The exact timing numbers depend on your machine. The `timeit` lines are part of the script; just run it and you’ll see the real timings.

---

## 6) Real‑World Use Cases (a few important ones)

1. **Stock / price streams**
   For each day, find the farthest later day with a **lower** price (earliest point to exit a long position with loss). Useful for risk analysis or stress back‑testing heuristics.

2. **Quality control / sensor thresholds**
   In a sequence of measurements, for each reading identify the **farthest later** reading that drops below the current reading — helps spot longest “recovery window” before a significant degradation reoccurs.

3. **Gaming & leaderboards**
   For a player’s score at time `i`, find the farthest later event where a lower score occurs (e.g., to cap streaks or define “decay windows” over which a player stayed above a threshold).

4. **Log analysis**
   In latency traces, for each spike time `i`, locate the farthest later time where latency dips below the spike level — to measure worst‑case duration until “healthy” performance returns.
