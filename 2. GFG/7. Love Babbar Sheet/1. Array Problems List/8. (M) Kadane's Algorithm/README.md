# Kadane's Algorithm

**Difficulty:** Medium
**Accuracy:** 36.28%
**Submissions:** 1.1M
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given an integer array `arr[]`. You need to find the **maximum** sum of a subarray.

---

## Examples

### Example 1

* **Input:** `arr[] = [2, 3, -8, 7, -1, 2, 3]`
* **Output:** `11`
* **Explanation:** The subarray `{7, -1, 2, 3}` has the largest sum `11`.

### Example 2

* **Input:** `arr[] = [-2, -4]`
* **Output:** `-2`
* **Explanation:** The subarray `{-2}` has the largest sum `-2`.

### Example 3

* **Input:** `arr[] = [5, 4, 1, 7, 8]`
* **Output:** `25`
* **Explanation:** The subarray `{5, 4, 1, 7, 8}` has the largest sum `25`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `-10^9 ≤ arr[i] ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Zoho, Flipkart, Morgan Stanley, Accolite, Amazon, Microsoft, Samsung, Snapdeal, 24\*7 Innovation Labs, Citrix, D-E-Shaw, FactSet, Hike, Housing.com, MetLife, Ola Cabs, Oracle, Payu, Teradata, Visa, Walmart, Adobe, Google, Arcesium

---

## Topic Tags

Arrays, Dynamic Programming, Data Structures, Algorithms

---

## Related Interview Experiences

* Oracle Interview Experience Set 45 For 3 Years Experienced
* Zoho Interview Experience Set 18 On Campus
* Hike Interview Experience Set 5
* Ola Interview Experience Set 10 Ds
* Accolite Interview Experience Set 3 On Campus
* Microsoft Interview Experience Set 151 Sde 2 3 5 Years Experience
* Microsoft Interview Experience For Internship 4
* Adobe Shecodes Product Interview Experience For Internship 2020

---

## Related Articles

* [Largest Sum Contiguous Subarray](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)

---

---
Let’s make Kadane’s Algorithm interview-ready: clear intuition, a quick dry run, and both brute-force and optimal Python solutions (with the exact signature you asked for). I’ll also include the “what interviewers ask” section + a 10-second mnemonic.

---

## 2) Intuition + step-by-step dry run

### Problem

Given an integer array `arr[]`, find the **maximum possible sum of a contiguous subarray**.

### Core idea (Kadane)

Scan left→right keeping:

* `curr` = best sum **ending at** current index (either extend previous subarray or start fresh here).
* `best` = best sum **seen so far**.

Recurrence:

* `curr = max(arr[i], curr + arr[i])`
* `best = max(best, curr)`

This works because if the running sum `curr` ever goes negative, it can only hurt any future sum—so we “restart” at the next element.

### Dry run (example: `arr = [2, 3, -8, 7, -1, 2, 3]`)

Initialize: `curr = best = 2`

| i | arr[i] | curr = max(arr[i], curr+arr[i]) | best |
| - | ------ | ------------------------------- | ---- |
| 0 | 2      | max(2, 2) = 2                   | 2    |
| 1 | 3      | max(3, 5) = 5                   | 5    |
| 2 | -8     | max(-8, -3) = -3                | 5    |
| 3 | 7      | max(7, 4) = 7                   | 7    |
| 4 | -1     | max(-1, 6) = 6                  | 7    |
| 5 | 2      | max(2, 8) = 8                   | 8    |
| 6 | 3      | max(3, 11) = 11                 | 11   |

Answer: **11** (subarray `[7, -1, 2, 3]`)

Edge case (all negatives): Kadane still works if you initialize with `arr[0]`.
Example: `[-2, -4]` → output `-2`.

---

## 3) Python solutions (brute + optimal)

### A) Brute force (clear but slow): O(n²) time, O(1) space

```python
class Solution:
    def maxSubarraySum(self, arr):
        """
        Brute-force: consider every subarray, keep the max sum.
        Time  : O(n^2)
        Space : O(1)
        """
        n = len(arr)
        best = arr[0]
        for i in range(n):
            running = 0
            for j in range(i, n):
                running += arr[j]          # sum of arr[i..j]
                if running > best:
                    best = running
        return best
```

### B) Optimal (Kadane): O(n) time, O(1) space

```python
class Solution:
    def maxSubarraySum(self, arr):
        """
        Kadane's Algorithm.
        curr = best subarray sum ending at i
        best = best over all prefixes up to i
        Time  : O(n)
        Space : O(1)
        """
        curr = best = arr[0]
        for x in arr[1:]:
            curr = max(x, curr + x)   # extend or restart
            best = max(best, curr)    # track global best
        return best
```

### (Optional) Return also the subarray indices (often earns bonus points)

```python
class Solution:
    def maxSubarraySum(self, arr):
        """
        Kadane with start/end indices.
        Returns just the sum to match required signature, but shows how to capture segment.
        """
        curr = best = arr[0]
        start = best_l = best_r = 0   # current start; best [best_l..best_r]
        for i in range(1, len(arr)):
            if arr[i] > curr + arr[i]:
                curr = arr[i]
                start = i             # restart here
            else:
                curr += arr[i]        # extend

            if curr > best:
                best = curr
                best_l, best_r = start, i
        # You could print/use (best_l, best_r) if interviewer asks
        return best
```

---

## 4) Interview quick-memory + Q&A

### 10-second mnemonic

> **“Extend or Restart → Compare.”**
> (extend `curr + x` or restart at `x`, then update `best`)

### What interviewers often ask

**Q1. Why does Kadane work?**
> Because any prefix with negative sum decreases any future sum; dropping it can only help. Thus we reset when the running sum becomes worse than starting fresh.

**Q2. What about all negative numbers?**
> Initialize `curr = best = arr[0]`. This ensures the result is the **maximum (least negative)** element.

**Q3. Time/space complexity?**
> `O(n)` time, `O(1)` extra space.

**Q4. How to return the subarray itself?**
> Track the current start index, and whenever you update `best`, record `(best_l, best_r)`.

**Q5. Variants?**

> * Maximum **circular** subarray: compute max normal subarray and max “wrap” via total sum − min subarray.
> * 2D Kadane (maximum sum rectangle) → apply 1D Kadane over compressed columns.

**Q6. Dynamic programming formulation?**
> `dp[i] = max(arr[i], dp[i-1] + arr[i])`, answer is `max(dp)`. Kadane is just the space-optimized DP.

---

### Tiny checklist to say before coding

1. “I’ll use Kadane: `curr` and `best`.”
2. “At each step: `curr = max(x, curr+x)`; `best = max(best, curr)`.”
3. “Handles all negatives with `best = arr[0]`.”
4. “O(n) time, O(1) space.”

You’re set.

---

---


Absolutely—let’s close Kadane’s Algorithm with practical context and a runnable, timed script.

---

## 5) Real-World Use Cases (easy to relate)

* **Single buy–sell stock profit (on diffs):**
>  Convert prices to daily differences; the best single trade is the **max sum subarray** on those diffs.

* **Error/latency burst detection:**
>  Treat “improvement = baseline − latency”. The biggest contiguous improvement window is Kadane’s best subarray.

* **Engagement streaks:**
>  Map each day to a score (+ for good signals, − for bad). The **strongest streak** is the max sum subarray.

* **Network/CPU utilization peaks:**
>  After zero-centering the series, the **largest positive energy window** emerges as Kadane’s segment.

* **Revenue/retention uplift window (A/B):**
>  Daily deltas vs. control → contiguous period of **maximum uplift** is Kadane.

---

## 6) Full Program (with inline complexity notes + timings)

```python
#!/usr/bin/env python3
"""
Kadane's Algorithm: Maximum Subarray Sum
---------------------------------------
- Optimal time: O(n)
- Space: O(1)

This script:
  * Implements Kadane (and a brute-force reference)
  * Runs sample inputs
  * Times runs using perf_counter and timeit
"""

from time import perf_counter
import timeit
from typing import List


class Solution:
    def maxSubarraySum(self, arr: List[int]) -> int:
        """
        Kadane's Algorithm
        ------------------
        At each element x:
          - Either extend the previous subarray (curr + x) or start fresh at x
          - Update global best
        Time  : O(n)  — single pass
        Space : O(1)  — constant extra variables
        """
        curr = best = arr[0]          # O(1)
        for x in arr[1:]:             # O(n-1) ~ O(n)
            curr = max(x, curr + x)   # O(1)
            best = max(best, curr)    # O(1)
        return best


def brute_max_subarray_sum(arr: List[int]) -> int:
    """
    Brute-force reference (for validation)
    Consider all O(n^2) subarrays and track max sum.
    Time  : O(n^2)
    Space : O(1)
    """
    best = arr[0]
    n = len(arr)
    for i in range(n):                   # O(n)
        run = 0
        for j in range(i, n):            # O(n-i)
            run += arr[j]                # O(1)
            if run > best:
                best = run
    return best


# ------------------------ Timing helpers ------------------------

def time_single_run(func, *args, **kwargs):
    """Wall-clock one run. Overhead O(1)."""
    t0 = perf_counter()
    out = func(*args, **kwargs)
    t1 = perf_counter()
    return out, t1 - t0

def avg_time_with_timeit(stmt: str, globals_dict: dict, number: int = 5) -> float:
    """Average across 'number' runs using timeit."""
    return timeit.timeit(stmt, number=number, globals=globals_dict) / number


# ---------------------------- Demo ------------------------------

if __name__ == "__main__":
    samples = [
        [2, 3, -8, 7, -1, 2, 3],    # expected 11
        [-2, -4],                   # expected -2 (all negative)
        [5, 4, 1, 7, 8],            # expected 25 (whole array)
        [1, -3, 2, 1, -1, 3, -2],   # expected 5 (2+1-1+3)
    ]

    sol = Solution()

    print("Kadane's Algorithm — Maximum Subarray Sum\n")

    for arr in samples:
        # Validate against brute force for peace of mind
        brute_ans, t_brute = time_single_run(brute_max_subarray_sum, arr)
        kadane_ans, t_kadane = time_single_run(sol.maxSubarraySum, arr)

        print(f"Input:  {arr}")
        print(f"Brute:  {brute_ans}  (time: {t_brute*1e6:.1f} µs)")
        print(f"Kadane: {kadane_ans}  (time: {t_kadane*1e6:.1f} µs)")
        print("-" * 56)

    # Larger randomized-like case for average timing
    big = [(-1)**i * (i % 7) for i in range(200000)]  # length 200k

    stmt = "Solution().maxSubarraySum(big)"
    avg = avg_time_with_timeit(stmt, globals_dict={"Solution": Solution, "big": big}, number=5)
    print(f"\nAverage Kadane time on 200k elements over 5 runs: {avg:.6f} s")

    print("\nComplexity (Kadane):")
    print("  Time  : O(n)")
    print("  Space : O(1)")
```

### What you’ll see (example)

```
Kadane's Algorithm — Maximum Subarray Sum

Input:  [2, 3, -8, 7, -1, 2, 3]
Brute:  11  (time: 3xx.xx µs)
Kadane: 11  (time: 2x.xx µs)
--------------------------------------------------------
Input:  [-2, -4]
Brute:  -2  (time: 2x.xx µs)
Kadane: -2  (time: 1x.xx µs)
--------------------------------------------------------
...

Average Kadane time on 200k elements over 5 runs: 0.0xx s

Complexity (Kadane):
  Time  : O(n)
  Space : O(1)
```

---

### Interview one-liner to say before coding

> “I’ll use **Kadane’s Algorithm**: at each step I either **extend or restart** the current subarray, and keep a **global best**. That’s **O(n) time, O(1) space**, and it naturally handles all-negative arrays by initializing with `arr[0]`.”

---

---

Excellent — this is one of the **most fundamental and beautiful algorithms** in computer science interviews, and understanding *why it works* makes you instantly stronger at dynamic programming and array problems.

Let’s go step by step 👇

---

## 💡 **Definition — What is Kadane’s Algorithm?**

> **Kadane’s Algorithm** is a **dynamic programming / greedy** algorithm used to find the **maximum sum of any contiguous subarray** in a one-dimensional array (which can have positive and negative numbers).

So if you’re given an array:

```
arr = [2, 3, -8, 7, -1, 2, 3]
```

Kadane’s Algorithm finds that the **subarray [7, -1, 2, 3]** has the largest possible sum = **11**.

---

## ⚙️ **The Intuition — Why it Works**

Imagine scanning the array **from left to right**, keeping track of:

* The **current best subarray sum** ending *right here*, and
* The **global best sum** seen so far.

We make a simple observation:

> If the running sum ever becomes negative, it can only hurt any future subarray.
> So, we discard it (reset the sum) and start fresh from the next element.

In other words:

* **Continue adding** if the sum stays positive.
* **Restart** if it drops below zero.

---

## 🧩 **Recurrence Relation (the core formula)**

Let:

* `curr_sum` = maximum subarray sum ending at current index
* `max_sum` = maximum sum found so far

Then:

```
curr_sum = max(arr[i], curr_sum + arr[i])
max_sum  = max(max_sum, curr_sum)
```

You can interpret this as:

> At every step, either **extend** the existing subarray or **start a new one**.

---

## 🔁 **Step-by-Step Example**

Let’s dry run on:

```
arr = [2, 3, -8, 7, -1, 2, 3]
```

| i | arr[i] | curr_sum = max(arr[i], curr_sum + arr[i]) | max_sum |
| - | ------ | ----------------------------------------- | ------- |
| 0 | 2      | 2                                         | 2       |
| 1 | 3      | 5                                         | 5       |
| 2 | -8     | -3                                        | 5       |
| 3 | 7      | 7                                         | 7       |
| 4 | -1     | 6                                         | 7       |
| 5 | 2      | 8                                         | 8       |
| 6 | 3      | 11                                        | 11      |

✅ **Result = 11**

---

## 🧠 **Simplified Intuition**

Think of walking through the array carrying a “running happiness meter.”

* If you feel negative overall, drop that baggage and start again.
* Keep the best happiness level ever reached.
  That’s Kadane in plain English.

---

## ⚡ **Pseudocode (5 lines you can recall easily)**

```
function maxSubarraySum(arr):
    curr = best = arr[0]
    for x in arr[1:]:
        curr = max(x, curr + x)   # extend or restart
        best = max(best, curr)
    return best
```

---

## ⏱️ **Complexities**

| Metric    | Value | Why                    |
| --------- | ----- | ---------------------- |
| **Time**  | O(n)  | One pass through array |
| **Space** | O(1)  | Only two variables     |

---

## 📦 **When to Use Kadane’s Algorithm**

Use Kadane’s whenever you see:

* “Maximum sum of a subarray / contiguous segment.”
* “Best period / streak / profit / performance.”
* Or any question hinting: “You can’t reorder elements.”

---

## 🌍 **Real-World Analogies / Applications**

| Context                     | How it maps to Kadane                                            |
| --------------------------- | ---------------------------------------------------------------- |
| 📈 **Stock trading**        | Max profit from one buy-sell (apply Kadane on price differences) |
| 💰 **Revenue tracking**     | Best contiguous period of profit                                 |
| 🧠 **Signal processing**    | Strongest contiguous positive energy burst                       |
| 📊 **Analytics dashboards** | Maximum streak of growth or engagement                           |
| 🎮 **Gaming**               | Longest “winning streak” based on score deltas                   |

---

## 🎯 **Interview Soundbite (say this confidently)**

> “Kadane’s Algorithm is a linear-time dynamic programming approach to find the maximum sum of a contiguous subarray.
> It keeps a running sum and resets it when it becomes negative, because a negative prefix can only reduce future sums.”

---

## 🧠 **Mnemonic to Recall Quickly**

> **“Extend or Restart → Compare → Return.”**

That’s all you need to rebuild Kadane’s in 30 seconds during an interview.

---

✅ **In One Line (summary):**

> Kadane’s Algorithm scans the array once, keeping a running maximum and resetting when it becomes negative — resulting in an O(n), O(1)-space solution for the maximum subarray sum.
