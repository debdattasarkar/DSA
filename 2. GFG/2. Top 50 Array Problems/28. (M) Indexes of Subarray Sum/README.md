# Indexes of Subarray Sum

**Difficulty:** Medium
**Accuracy:** 16.5%
**Submissions:** 1.8M+
**Points:** 4
**Average Time:** 20m

---

Given an array `arr[]` containing only **non-negative** integers, your task is to find a **continuous subarray** (a contiguous sequence of elements) whose **sum equals** a specified value `target`. You need to return the **1-based indices** of the **leftmost** and **rightmost** elements of this subarray. **Return the first subarray** whose sum equals the target.

**Note:** If no such subarray is possible then, return `[-1]`.

---

## Examples

### Example 1

**Input:** `arr[] = [1, 2, 3, 7, 5], target = 12`
**Output:** `[2, 4]`
**Explanation:** The sum of elements from 2nd to 4th position is 12.

### Example 2

**Input:** `arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15`
**Output:** `[1, 5]`
**Explanation:** The sum of elements from 1st to 5th position is 15.

### Example 3

**Input:** `arr[] = [5, 3, 4], target = 2`
**Output:** `[-1]`
**Explanation:** There is no subarray with sum 2.

---

## Constraints

* `1 <= arr.size() <= 10^6`
* `0 <= arr[i] <= 10^3`
* `0 <= target <= 10^9`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Amazon, Facebook, Google, Visa

## Topic Tags

Algorithms, Arrays, Data Structures, Prefix-sum, Searching, Sliding-window

## Related Articles

* [Find Subarray With Given Sum](https://www.geeksforgeeks.org/find-subarray-with-given-sum/)


---

---

Below is a tight, interview-style guide for “Indexes of Subarray Sum”.

---

## 2) Explanation + Step-by-Step Dry Run

**Task (non-negative array):**
Find the **first** (leftmost) continuous subarray whose sum equals `target`. Return **1-based** `[L, R]`. If none, return `[-1]`.

**Most asked approach: Sliding Window (Two Pointers)**
Because all numbers are **non-negative**, the window sum only **increases** when we move the right pointer and **decreases** when we move the left pointer. So we can expand/shrink a window to match the target in **O(n)**.

**Algorithm**

1. `l = 0`, `curr = 0`.
2. For each `r` from `0..n-1`:

   * Add `arr[r]` to `curr`.
   * While `curr > target` and `l <= r`, shrink from left: `curr -= arr[l]`, `l += 1`.
   * If `curr == target`, return `[l+1, r+1]` (1-based).
3. If we finish the loop, return `[-1]`.

This naturally returns the **first** subarray (we only move `l` forward when we must).

**Dry run** — `arr = [1, 2, 3, 7, 5]`, `target = 12`

* Start: `l=0, curr=0`
* `r=0` → `curr=1` (<12)
* `r=1` → `curr=3` (<12)
* `r=2` → `curr=6` (<12)
* `r=3` → `curr=13` (>12) → shrink: remove `arr[0]=1` ⇒ `curr=12`, `l=1`
  Now `curr == 12` ⇒ return **\[2, 4]**.

---

## 3) Python Solutions (Brute → Optimized)

### A) Brute Force (clear but slow): O(n²) time, O(1) space

```python
# User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        # Try all starts i, and grow j to the right
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += arr[j]
                if s == target:
                    return [i + 1, j + 1]  # 1-based
        return [-1]
```

### B) Optimal for Non-Negative Arrays: Sliding Window

**Time:** O(n) | **Space:** O(1)

```python
# User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        l = 0
        curr = 0

        for r in range(n):
            curr += arr[r]                      # expand window

            while l <= r and curr > target:     # shrink until <= target
                curr -= arr[l]
                l += 1

            if curr == target:                  # found earliest such window
                return [l + 1, r + 1]           # 1-based indices

        return [-1]
```

> **Edge cases:**
> • `target == 0`: returns single zero if present (e.g., `[0]` → `[i+1, i+1]`), else `[-1]`.
> • Large `n` (up to 1e6) → O(n) is crucial; sliding window fits.

### C) Bonus (works with **negatives** too): Prefix Sum + HashMap

(Not required here; shown for completeness when the array can have negatives.)

```python
# User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # Works for any integers by using prefix sums.
        # Time: O(n), Space: O(n)
        pref_idx = {0: -1}                 # sum -> earliest index
        s = 0

        for i, x in enumerate(arr):
            s += x
            need = s - target
            if need in pref_idx:
                start = pref_idx[need] + 1 # 0-based start
                return [start + 1, i + 1]  # 1-based [L, R]
            # store earliest occurrence only
            if s not in pref_idx:
                pref_idx[s] = i

        return [-1]
```

---

## 4) Interview Q & A

**Q1. Why does sliding window require non-negative numbers?**
Because when all numbers are ≥ 0, increasing the window (move `r`) never decreases the sum, and shrinking it (move `l`) never increases the sum. That monotonicity makes the two-pointer logic valid.

**Q2. What if the array can contain negatives?**
Use the **prefix-sum hash map** approach (Solution C). Sliding window can fail with negatives.

**Q3. How do you ensure you return the *first* subarray?**
In sliding window, we only advance `l` to reduce sum when necessary; the first time we hit `target`, the window is the earliest starting position for that `r`. This yields the leftmost solution.

**Q4. Complexity?**

* Brute force: O(n²) time, O(1) space.
* Sliding window: O(n) time, O(1) space.
* Prefix-sum hashmap: O(n) time, O(n) space.

**Q5. What about `target = 0`?**
With non-negative arrays, only windows of zeros qualify. The sliding window code above returns a single-element zero window if present, otherwise `[-1]`.

**Q6. Why seed the hashmap with `0: -1` (in Solution C)?**
So that if the sum from index 0..i equals `target`, we can produce a window starting at index 0 (1-based: `[1, i+1]`).

---

---

Below is a complete, runnable Python program that:

* Implements the **O(n)** sliding-window solution for non-negative arrays (required by the problem).
* Also includes a **brute-force** (O(n²)) checker for comparison (kept for interviews).
* Shows **inputs and outputs**.
* Uses **`timeit`** to measure runtime inline in the main program.
* Has rich inline comments with **time & space complexity** notes.

```python
#!/usr/bin/env python3
"""
Indexes of Subarray Sum (non-negative array)
--------------------------------------------
Given an array of non-negative integers `arr` and a target sum `target`,
return the 1-based indices [L, R] of the *first* continuous subarray whose
sum equals target. If no such subarray exists, return [-1].

Primary approach used here: Sliding Window / Two Pointers
    Time Complexity (overall): O(n) — each index enters/leaves the window at most once
    Space Complexity: O(1) — a few scalars

Also included:
    Brute-force method for validation / interviews
        Time Complexity: O(n^2) worst case
        Space Complexity: O(1)
"""

from timeit import timeit
import random


class Solution:
    def subarraySum(self, arr, target):
        """
        Sliding window for NON-NEGATIVE arrays.

        Invariants:
        - Window is [l, r], inclusive.
        - 'curr' holds the sum in the window.
        - Since all nums are >= 0, expanding r never decreases 'curr',
          and shrinking l never increases 'curr'.

        Steps per iteration are O(1) amortized; each element is added once
        and removed at most once, giving O(n) total time. Additional space is O(1).
        """
        l = 0                # O(1) space
        curr = 0             # O(1) space

        # Iterate r from 0..n-1, each r processed once => O(n)
        for r, x in enumerate(arr):
            curr += x        # expand window, O(1)

            # While sum too big, shrink from the left; each l moves at most n steps total
            while l <= r and curr > target:
                curr -= arr[l]   # remove leftmost, O(1)
                l += 1           # move left pointer, O(1)

            # Check for success
            if curr == target:
                # Return 1-based indices; O(1)
                return [l + 1, r + 1]

        # If we finish without finding a window
        return [-1]


# --------- Extra (for interview contrast): Brute Force O(n^2) ----------
def subarray_sum_bruteforce(arr, target):
    """
    Try all starts i and extend to the right.
    Time: O(n^2) in worst case (two nested loops)
    Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == target:
                return [i + 1, j + 1]  # 1-based
    return [-1]


# ------------------------------- Main ----------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Test inputs (from the prompt/examples + some edge checks)
    tests = [
        # (arr, target, expected)
        ([1, 2, 3, 7, 5], 12, [2, 4]),      # sample: 2..4 sums to 12
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15, [1, 5]),  # 1..5 sums to 15
        ([5, 3, 4], 2, [-1]),               # no such subarray
        ([0, 0, 5], 0, [1, 1]),             # first zero (non-negative rule)
        ([0, 1, 2, 0, 3], 3, [3, 5]),       # 2 + 0 + 3
    ]

    print("=== Outputs (Sliding Window) ===")
    for arr, target, expected in tests:
        res = sol.subarraySum(arr, target)
        print(f"arr={arr}, target={target} -> {res} (expected {expected})")

    # Quick side-by-side correctness check on small arrays:
    print("\n=== Brute Force cross-check on small arrays ===")
    small_tests = [
        ([1, 1, 1, 1], 2),
        ([2, 2, 2], 4),
        ([3, 1, 2, 1, 1], 3),
        ([5, 1, 2], 8),
    ]
    for arr, target in small_tests:
        fast = sol.subarraySum(arr, target)
        slow = subarray_sum_bruteforce(arr, target)
        print(f"arr={arr}, target={target} -> fast={fast}, brute={slow}")

    # ---------------- Timing with timeit ----------------
    # We measure time for the SLIDING WINDOW approach on a mid-sized array
    print("\n=== Timing (timeit) ===")
    # Generate a non-negative array (constraint-aligned) of moderate size
    random.seed(7)
    big_arr = [random.randint(0, 10) for _ in range(100_000)]  # values 0..10
    big_target = 250  # some target to search for

    # Measure the sliding-window solution time
    t_sw = timeit(lambda: sol.subarraySum(big_arr, big_target), number=20)
    print(f"Sliding Window on n=100000, 20 runs: {t_sw:.4f} seconds")

    # For fairness, don't time brute force on large n (it’s too slow O(n^2)).
    # Instead, show on small n:
    small_arr = [random.randint(0, 10) for _ in range(1000)]
    small_target = 50
    t_brut = timeit(lambda: subarray_sum_bruteforce(small_arr, small_target), number=3)
    print(f"Brute Force on n=1000, 3 runs:     {t_brut:.4f} seconds")

    # Sample final call to display a result for the big case:
    final_res = sol.subarraySum(big_arr, big_target)
    print(f"\nFinal sample result on big_arr (target={big_target}): {final_res}")

"""
Notes on complexities (in-place, step-by-step):
- Setting l=0, curr=0: O(1) time, O(1) space.
- For loop over r=0..n-1: O(n) iterations total.
  * Each iteration does O(1) amortized work (adds arr[r], maybe shrinks l).
  * While loop across all iterations moves l at most n times => total O(n).
- Returning indices is O(1).
- Therefore total time is O(n); space is O(1).
"""
```

---

## 6) Real-World Use Cases (a few important ones)

1. **Payment streams / fraud windows:**
   Detect the first time a running total of transactions hits a specific threshold (e.g., cumulative spend equals a configured limit) — non-negative amounts suit sliding window.

2. **Network throughput / rate-limiting:**
   Find the earliest contiguous block of request sizes whose sum meets a quota to trigger throttling or provisioning.

3. **Telemetry & IoT batching:**
   Aggregate sensor readings into chunks that reach a target payload size for transmission while preserving order.

4. **Log ingestion / file chunking:**
   Build contiguous file/log chunks of a target byte-size for storage or processing pipelines (entries are non-negative lengths).
