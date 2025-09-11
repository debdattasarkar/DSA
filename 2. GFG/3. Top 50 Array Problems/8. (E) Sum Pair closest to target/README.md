# Sum Pair Closest to Target

**Difficulty:** Easy
**Accuracy:** 44.75%
**Submissions:** 69K+
**Points:** 2

---

## Problem Statement

Given an array `arr[]` and a number `target`, find a pair of elements `(a, b)` in `arr[]`, where `a ≤ b`, whose **sum is closest to target**.

**Note:**

* Return the pair in **sorted order**.
* If there are **multiple** such pairs equally close to the target, **return the pair with maximum absolute difference** (`|a - b|`).
* If **no such pair** exists, return an **empty array**.

---

## Examples

### Example 1

**Input:** `arr[] = [10, 30, 20, 5]`, `target = 25`
**Output:** `[5, 20]`
**Explanation:** `5 + 20 = 25` is closest to `25`.

---

### Example 2

**Input:** `arr[] = [5, 2, 7, 1, 4]`, `target = 10`
**Output:** `[2, 7]`
**Explanation:** `(4, 5), (2, 7)` and `(4, 7)` are closest to `10`, but `|2 - 7| = 5` is the **maximum** among ties. Hence, return `[2, 7]`.

---

### Example 3

**Input:** `arr[] = [10]`, `target = 10`
**Output:** `[]`
**Explanation:** The array has only one element, so no pair can be formed.

---

## Constraints

* `1 ≤ arr.size() ≤ 2 * 10^5`
* `0 ≤ target ≤ 2 * 10^5`
* `0 ≤ arr[i] ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Ola Cabs

---

## Topic Tags

* Arrays
* Data Structures
* two-pointer-algorithm

---

## Related Articles

* [2 Sum Pair Sum Closest To Target](https://www.geeksforgeeks.org/2-sum-pair-sum-closest-to-target/)
* [Given Sorted Array Number X Find Pair Array Whose Sum Closest X](https://www.geeksforgeeks.org/given-sorted-array-number-x-find-pair-array-whose-sum-closest-x/)


---

---

Here’s a tight, interview-ready guide for **“Sum pair closest to target (with max |a−b| tie-break)”**.

---

## 2) Intuition + step-by-step dry run

### Core idea

* If you **sort** the array, the **two-pointer** sweep finds the closest sum in **O(n)**:

  * Start `i=0` (smallest), `j=n-1` (largest).
  * Let `s = arr[i] + arr[j]`.

    * If `s` is **closer** to `target` than our best, update the answer.
    * If `|s-target|` ties the best, pick the pair with **larger absolute difference** `|arr[j]-arr[i]|` (problem’s rule).
  * Move the pointer that helps push the sum toward the target:
    `s < target ⇒ i += 1`, `s > target ⇒ j -= 1`.
    (If `s == target`, we still evaluate/update, then move either side; moving both would also work.)

This works because with the array sorted, increasing the left value or decreasing the right value moves the sum monotonically.

### Dry run 1

`arr = [10, 30, 20, 5], target = 25`
Sort → `[5, 10, 20, 30]`

* `i=0 (5)`, `j=3 (30)`, `s=35`, `|35-25|=10` → best = `[5,30]`
* `s > target`, `j=2`
* `i=0 (5)`, `j=2 (20)`, `s=25`, `|25-25|=0` → better → best = `[5,20]`
* `s == target`, move (say) `j=1`; now `i<j` fails → stop
  **Answer:** `[5,20]`.

### Dry run 2 (tie-break demo)

`arr = [5, 2, 7, 1, 4], target = 10`
Sort → `[1,2,4,5,7]`
Check pairs during sweep that are closest (sum 9 or 11 → diff 1):

* Close pairs: `(4,5)` (diff 1, |a-b|=1), `(2,7)` (diff 1, |a-b|=5), `(4,7)` (diff 1, |a-b|=3).
  Tie-break picks **max |a−b| ⇒ \[2,7]**.

### Edge case

If `len(arr) < 2` → return `[]`.

---

## 3) Python solutions (brute & optimized), with interview-style comments

### A) Two-pointer after sort — **expected solution**

```python
class Solution:
    def sumClosest(self, arr, target):
        """
        Return the pair [a, b] (a <= b) whose sum is closest to target.
        Tie-break: if multiple are equally close, pick the pair with
                    larger |a - b|.
        If no pair exists (n < 2), return [].

        Time:  O(n log n) due to sorting
        Space: O(1) extra (ignoring output)
        """
        n = len(arr)
        if n < 2:
            return []

        arr.sort()  # O(n log n)

        i, j = 0, n - 1
        best_pair = []
        best_diff = float('inf')   # difference in sum from target
        best_gap  = -1             # |a - b| to resolve ties

        while i < j:
            a, b = arr[i], arr[j]
            s = a + b
            diff = abs(s - target)
            gap  = b - a           # arr sorted ⇒ b >= a

            # Update if strictly better, or tie with larger |a-b|
            if (diff < best_diff) or (diff == best_diff and gap > best_gap):
                best_diff = diff
                best_gap  = gap
                best_pair = [a, b]

            # Move pointers toward the target
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                # s == target -> perfect; still continue to respect tie-break
                # but typical early exit is fine if tie-break doesn't matter.
                # We'll adjust both sides to look for wider gap at same diff=0.
                i += 1
                j -= 1

        return best_pair
```

### B) Binary search per element — **clean O(n log n) alternative**

```python
import bisect

class Solution:
    def sumClosest(self, arr, target):
        """
        For each index i, look for value near (target - arr[i]) via binary search.
        Check candidate positions idx and idx-1 to catch nearest.
        Time:  O(n log n) (sort + n * log n)
        Space: O(1) extra
        """
        n = len(arr)
        if n < 2:
            return []

        arr.sort()  # O(n log n)

        best_pair = []
        best_diff = float('inf')
        best_gap  = -1

        for i in range(n - 1):
            need = target - arr[i]
            # Search in the right side to avoid using the same element twice
            idx = bisect.bisect_left(arr, need, i + 1, n)

            # Check arr[idx] and arr[idx-1] if they are valid
            for cand_idx in (idx, idx - 1):
                if i < cand_idx < n:
                    a, b = arr[i], arr[cand_idx]
                    s = a + b
                    diff = abs(s - target)
                    gap  = b - a
                    if (diff < best_diff) or (diff == best_diff and gap > best_gap):
                        best_diff = diff
                        best_gap  = gap
                        best_pair = [a, b]

        return best_pair
```

### C) Brute force — **simple but slow (for completeness)**

```python
class Solution:
    def sumClosest(self, arr, target):
        """
        Try every pair; keep best by diff, then by |a-b|.
        Time:  O(n^2)
        Space: O(1)
        """
        n = len(arr)
        if n < 2:
            return []
        best_pair = []
        best_diff = float('inf')
        best_gap  = -1

        for i in range(n):
            for j in range(i + 1, n):
                a, b = sorted((arr[i], arr[j]))
                s = a + b
                diff = abs(s - target)
                gap  = b - a
                if (diff < best_diff) or (diff == best_diff and gap > best_gap):
                    best_diff = diff
                    best_gap  = gap
                    best_pair = [a, b]
        return best_pair
```

---

## 4) Likely interviewer Q\&A

**Q1. Why does the two-pointer method work after sorting?**
Because as you move the left pointer rightwards, sums **increase**; moving the right pointer leftwards, sums **decrease**. This monotonicity ensures that adjusting pointers always moves the sum toward the target without missing optimal pairs.

**Q2. How do you enforce the tie-break (max |a−b|)?**
Whenever we see an equal closeness (`diff == best_diff`), we pick the pair with **larger `gap = b - a`** (array is sorted so `b ≥ a`).

**Q3. Edge cases?**

* Fewer than 2 elements → `[]`.
* Duplicates are fine—comparison and tie-break logic still holds.
* If many pairs have exactly the target sum, we return the one with **largest |a−b|**.

**Q4. Complexity?**

* Two-pointer: **O(n log n)** time (sort dominates), **O(1)** extra space.
* Binary-search per element: also **O(n log n)**, **O(1)** extra.
* Brute force: **O(n²)**.

**Q5. Can we early-exit on exact sum?**
If tie-break didn’t exist, yes (finding `diff = 0` could end). With the **max |a−b|** tie-break, we may choose to keep searching for another exact sum with a **wider gap**; the provided two-pointer code does that by moving **both pointers** when `s == target`.

**Q6. What if the array is already sorted?**
Skip sorting to get **O(n)** time with the two-pointer scan.

---

---

All set! I executed a **complete inline Python program** that:

* Implements `sumClosest` using the **two-pointer** method (`O(n log n)` time, `O(1)` extra space), plus **bisect** and **bruteforce** alternatives.
* Shows outputs for the examples, several edge cases, and a **large benchmark** with **timeit** timings.
* Reuses the exact tie-break rule: when multiple sums are equally close to the target, it returns the pair with the **maximum |a−b|**.

You can copy the code from the output cell to run locally.

---

## 6) Real-World Use Cases (high-impact)

* **Closest deal/price pairing:** Given a target budget, pick two prices whose sum is closest; prefer widely spaced items (e.g., one high-ticket + one low-ticket) when ties occur to diversify.
* **Ad/campaign allocation:** Choose two campaign spends that hit a daily cap as closely as possible; tie-break for wider spread to explore extremes.
* **Portfolio hedging:** Pair a long and a short (nonnegative weights) to match a target net exposure; wider |a−b| tie-break yields stronger hedge separation.
* **Bin packing heuristic:** When packing two items per bin, pick a pair closest to capacity to reduce waste; the tie-break can encourage using one large + one small item.
* **Latency SLO blending:** Combine two service tiers so their latencies sum closest to an SLO; tie-break to mix very fast + much slower for cost optimization.
