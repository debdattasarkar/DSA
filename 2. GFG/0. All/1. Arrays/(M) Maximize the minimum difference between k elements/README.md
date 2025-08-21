
---

# Maximize the minimum difference between k elements

**Difficulty:** Medium
**Accuracy:** 80.6%
**Submissions:** 41K+
**Points:** 4

---

## Problem Statement

Given an array `arr[]` of integers and an integer `k`, select `k` elements from the array such that the **minimum absolute difference** between any two of the selected elements is **maximized**.

Return this **maximum possible minimum difference**.

---

## Examples

**Example 1:**

```
Input: arr[] = [2, 6, 2, 5], k = 3
Output: 1
Explanation: 
3 elements out of 4 elements are to be selected with a minimum difference as large as possible.  
Selecting 2, 2, 5 will result in minimum difference as 0.  
Selecting 2, 5, 6 will result in minimum difference as 6 - 5 = 1.
```

**Example 2:**

```
Input: arr[] = [1, 4, 9, 0, 2, 13, 3], k = 4
Output: 4
Explanation: 
Selecting 0, 4, 9, 13 will result in minimum difference of 4, which is the largest minimum difference possible.
```

---

## Constraints

* $1 \leq arr.size() \leq 10^5$
* $0 \leq arr[i] \leq 10^6$
* $2 \leq k \leq arr.size()$

---

## Expected Complexities

* **Time Complexity:** $O(n \log n)$
* **Auxiliary Space:** $O(1)$

---

## Topic Tags

* Binary Search
* Sorting
* Arrays

---

## Related Articles

* [Maximize The Minimum Difference Between Any Element Pair By Selecting K Elements From Given Array](https://www.geeksforgeeks.org/maximize-the-minimum-difference-between-any-element-pair-by-selecting-k-elements-from-given-array/)

---

---

Here’s a crisp, interview‑ready package for **Maximize the minimum difference between k elements**.

---

# 2) Explanation + Step‑by‑step dry run

## Idea in one line

If we sort the array, the answer is the largest distance **D** such that you can pick **k** elements (from left to right) where every picked element is at least **D** apart from the previous picked one.

## Why sorting + binary search works

* After sorting, if a minimum gap **D** is feasible (we can pick **k** elements), then any **D' ≤ D** is also feasible.
  → This monotonicity lets us binary search on **D**.
* To test feasibility for a fixed **D**, a **greedy** scan works: take the first number, then always take the next number that is at least **D** away from the last taken. If we end up taking **k** numbers, **D** is feasible.

Time: sort $O(n \log n)$, binary search over range $[0, \max-\min]$ with each check $O(n)$ → $O(n \log n)$.

### Dry run on:

```
arr = [1, 4, 9, 0, 2, 13, 3], k = 4
Sorted: [0, 1, 2, 3, 4, 9, 13]
Search D in [0, 13] (max-min = 13)
```

Binary search iterations (lo, hi are inclusive; mid = (lo+hi)//2):

1. **lo=0, hi=13, mid=6**
   Greedy pick with D=6:

   * take 0
   * 1 (no), 2 (no), 3 (no), 4 (no), 9 (yes, 9-0=9 ≥6), 13 (no, 13-9=4 <6)
     → picked 2 elements (<4) ⇒ **not feasible**, set hi=5.

2. **lo=0, hi=5, mid=2**
   Greedy with D=2:

   * take 0
   * 1 (no), 2 (yes), 3 (no), 4 (yes), 9 (yes)
     → picked 4 elements ⇒ **feasible**, store ans=2, set lo=3.

3. **lo=3, hi=5, mid=4**
   Greedy with D=4:

   * take 0
   * 1 (no), 2 (no), 3 (no), 4 (yes), 9 (yes), 13 (no)
     → picked 3 elements (<4) ⇒ **not feasible**, set hi=3.

4. **lo=3, hi=3, mid=3**
   Greedy with D=3:

   * take 0
   * 1 (no), 2 (no), 3 (yes), 4 (no), 9 (yes), 13 (no)
     → picked 3 elements (<4) ⇒ **not feasible**, set hi=2.

Stop (lo>hi). Best stored answer = **2**? Wait—example’s output is **4** for k=4 with picks \[0,4,9,13].
Let’s re‑check step 3 (D=4):

* take 0
* 1 (no), 2 (no), 3 (no), 4 (yes, 4-0=4), 9 (yes, 9-4=5), 13 (yes, 13-9=4)
  → picked **4** elements! So D=4 **is feasible**.

(That’s the correct greedy trace; above I mistakenly skipped 13 with D=4.)

Corrected iteration 3:

* **D=4 feasible**, store ans=4, set lo=5.

5. **lo=5, hi=5, mid=5**

   * take 0 → 4 (no), 9 (yes), 13 (no; 13-9=4<5) → picked 2 elements → **not feasible**; hi=4.

Stop. Best answer = **4** ✅

---

# 3) Python solutions (brute → optimized)

## A) Brute force (use only for tiny n)

Try every k‑subset, compute its minimum pairwise difference, and keep the max. This is exponential; it’s purely pedagogical.

```python
from itertools import combinations

class Solution:
    def maxMinDiff(self, arr, k):
        # Edge: k <= 1 → min pairwise difference is "undefined"; conventionally 0
        if k <= 1:
            return 0
        best = 0
        # Try all k-element subsets (O(C(n,k)) subsets)
        for subset in combinations(arr, k):
            s = sorted(subset)
            # min adjacent diff inside the sorted subset
            mind = min(s[i+1] - s[i] for i in range(k - 1))
            best = max(best, mind)
        return best
```

* **Time:** $O(\binom{n}{k} \cdot k \log k)$  (intractable for big n)
* **Space:** $O(k)$ for a subset copy

## B) Optimized (expected in interviews): Sort + Binary Search + Greedy check

```python
class Solution:
    def maxMinDiff(self, arr, k):
        """
        Sort + binary search the answer.
        Time:  O(n log n) for sort + O(n log R) for search (R = max-min)  ~ O(n log n)
        Space: O(1) extra (in-place sort aside)
        """
        n = len(arr)
        if k <= 1 or n <= 1:
            return 0

        arr.sort()  # O(n log n)

        # Greedy feasibility: can we pick k numbers with pairwise gap >= D?
        def can_place(D: int) -> bool:
            count = 1               # pick the first element
            last = arr[0]
            for x in arr[1:]:
                if x - last >= D:   # place next as soon as gap allows
                    count += 1
                    last = x
                    if count == k:  # early exit
                        return True
            return False

        lo, hi = 0, arr[-1] - arr[0]
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_place(mid):
                ans = mid          # mid is feasible; try for a larger gap
                lo = mid + 1
            else:
                hi = mid - 1       # mid is too large; reduce
        return ans
```

**Why the greedy `can_place` is correct:** picking as early as possible never hurts (exchange argument). If some optimal solution delayed a pick when a feasible earlier one existed, swapping it earlier preserves feasibility and never reduces the room for the remaining picks.

---

# 4) Interview Q\&A (most common)

**Q1. Why does sorting not change the optimal answer?**
Because the minimum pairwise difference is determined by distances; ordering doesn’t change the set of pairwise distances. Sorting just lets us greedily pick from left to right.

**Q2. Why is the feasibility function monotonic?**
If you can place `k` elements with minimum gap `D`, then any `D' ≤ D` is easier; you can reuse the same placement or a laxer one.

**Q3. Why does the greedy placement (take earliest possible) work?**
If you ever skip an element that could be taken, taking it only increases the remaining slack for future placements. Formalized via an exchange argument.

**Q4. What are edge cases?**

* `k == 2`: answer is simply `max(arr) - min(arr)` (far ends).
* `k == n`: answer is the minimum adjacent difference in the sorted array.
* Duplicates: if duplicates exist, answer can be `0`.
* Very large array values → use integers; no floats.

**Q5. Time / Space?**

* Sorting dominates: $O(n \log n)$.
* Each binary search step scans once: $O(n)$, and there are $O(\log(\text{range}))$ steps.
* Extra space $O(1)$ (ignoring in‑place sort).

**Q6. Can you avoid sorting?**
Not realistically for this exact objective. Sorting unlocks the greedy structure; without it, feasibility checks become messy and slow.

**Q7. Could you binary search over indices instead of distances?**
No—what we need is the largest *distance* that is feasible, not a position. The monotone predicate lives over distances.

---

---

Here’s a **complete, runnable program** for **“Maximize the minimum difference between k elements”** with:

* Clean, interview‑ready optimized solution (Sort + Binary Search + Greedy).
* Inline comments calling out **time/space complexity for each step**.
* A tiny **main** that runs a couple of inputs and uses **`timeit`** to measure the end‑to‑end time.

```python
#!/usr/bin/env python3
"""
Problem:
Given an array arr[] and integer k, select k elements so that the
minimum absolute difference between ANY two selected elements is maximized.
Return that maximum possible minimum difference.

Approach (expected in interviews):
1) Sort the array.                          # O(n log n) time, O(1) extra (in-place)
2) Binary-search the answer D in [0, max-min].
3) For a fixed D, check feasibility by greedily picking from left to right:
   take the first element, then take next whenever gap >= D. Stop when we pick k.
   # O(n) per check, O(1) extra

Total complexity:
- Time  : O(n log n + n log R) ≈ O(n log n), where R = max(arr) - min(arr)
- Space : O(1) extra (ignoring Python’s sort implementation details)
"""

from timeit import timeit

class Solution:
    def maxMinDiff(self, arr, k):
        """
        Returns the largest D such that we can pick k elements from arr
        with pairwise minimum gap >= D.

        Parameters:
            arr (List[int]): array of integers (can be unsorted)
            k   (int)      : number of elements to pick

        Returns:
            int: maximum feasible minimum difference

        Overall:
            Time  : O(n log n) for sorting + O(n log R) for binary search checks
            Space : O(1) extra
        """
        n = len(arr)
        # Edge cases (constant time & space)
        if n <= 1 or k <= 1:
            return 0

        # ---- Step 1: Sort ----------------------------------------------------
        # Complexity: Time O(n log n), Space O(1) extra (in-place)
        arr.sort()

        # Greedy feasibility check: can we pick k items with min gap >= D?
        def can_place(D: int) -> bool:
            # Complexity: Time O(n), Space O(1)
            count = 1           # pick the first element
            last = arr[0]
            for x in arr[1:]:
                if x - last >= D:
                    count += 1
                    last = x
                    if count == k:     # early exit as soon as we placed k
                        return True
            return False

        # ---- Step 2: Binary search on the answer D ---------------------------
        # Search domain for D is [0, max(arr)-min(arr)]
        # Complexity: O(log R) iterations, each O(n) check => O(n log R)
        lo, hi = 0, arr[-1] - arr[0]
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_place(mid):
                ans = mid      # mid is feasible -> try for larger gap
                lo = mid + 1
            else:
                hi = mid - 1   # mid not feasible -> reduce
        return ans


# -------------------------- Demo / Timing -------------------------------------

def run_demo():
    sol = Solution()

    tests = [
        # (arr, k, expected)
        ([2, 6, 2, 5], 3, 1),
        ([1, 4, 9, 0, 2, 13, 3], 4, 4),     # from the prompt
        ([1, 3, 5, 7, 9], 2, 8),            # pick ends -> 9 - 1 = 8
        ([1, 1, 1, 1], 3, 0),               # duplicates -> min diff must be 0
        ([5], 1, 0),
    ]

    print("Running test cases...")
    for arr, k, exp in tests:
        got = sol.maxMinDiff(arr[:], k)   # use a copy; we sort in-place
        print(f"arr={arr}, k={k} -> answer={got}, expected={exp}")

    # --------------- timeit: Full program run timing -------------------------
    # We measure a single full call on the largest demo input above;
    # increase 'number' for finer measurements.
    arr_big = [1, 4, 9, 0, 2, 13, 3] * 1000
    k_big = 4
    def _bench():
        sol.maxMinDiff(arr_big[:], k_big)   # copy to include sort cost each run

    t = timeit(_bench, number=5)            # run 5 times
    print(f"\nTime for 5 runs on a 7k-element array: {t:.6f} seconds "
          f"(~{t/5:.6f} s per run)")

if __name__ == "__main__":
    run_demo()
```

### Sample Output (what you’ll see)

```
Running test cases...
arr=[2, 6, 2, 5], k=3 -> answer=1, expected=1
arr=[1, 4, 9, 0, 2, 13, 3], k=4 -> answer=4, expected=4
arr=[1, 3, 5, 7, 9], k=2 -> answer=8, expected=8
arr=[1, 1, 1, 1], k=3 -> answer=0, expected=0
arr=[5], k=1 -> answer=0, expected=0

Time for 5 runs on a 7k-element array: 0.0XXXX seconds (~0.0XXXX s per run)
```

---

## 6) Real‑World Use Cases (a few, high‑value)

1. **Wi‑Fi Access Point Placement / Sensor Deployment**
   Place **k** routers/sensors at existing candidate sites (the array) to **maximize the minimum separation**—reduces interference, improves coverage robustness.

2. **Manufacturing Tolerances / Quality Control**
   Pick **k** samples (from measured positions or times) with **maximized minimum spacing** to ensure even distribution across a production cycle for unbiased monitoring.

3. **Data Center Rack Allocation**
   Assign **k** high‑power servers to rack slots (predefined positions) to **maximize min distance** (thermal and power distribution constraints), improving cooling efficiency.

4. **Event Scheduling with Time Slots**
   Choose **k** sessions from available start times to maximize the minimal gap (breaks) between chosen sessions for logistics (room turnover, audience flow).

