# Maximum Product Subarray

**Difficulty:** Medium
**Accuracy:** 18.09%
**Submissions:** 451K+
**Points:** 4

---

## Problem Statement

Given an array `arr[]` that contains positive and negative integers (may contain `0` as well). Find the **maximum product** that we can get in a **subarray** of `arr[]`.

**Note:** It is guaranteed that the output fits in a 32-bit integer.

---

## Examples

### Example 1

**Input:** `arr[] = [-2, 6, -3, -10, 0, 2]`
**Output:** `180`
**Explanation:** The subarray with maximum product is `{6, -3, -10}` with product `6 * (-3) * (-10) = 180`.

### Example 2

**Input:** `arr[] = [-1, -3, -10, 0, 6]`
**Output:** `30`
**Explanation:** The subarray with maximum product is `{-3, -10}` with product `(-3) * (-10) = 30`.

### Example 3

**Input:** `arr[] = [2, 3, 4]`
**Output:** `24`
**Explanation:** For an array with all positive elements, the result is product of all elements.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `-10 ≤ arr[i] ≤ 10`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Morgan Stanley, Amazon, Microsoft, OYO Rooms, D-E-Shaw, Google

---

## Topic Tags

Arrays, Dynamic Programming, Data Structures, Algorithms

---

## Related Interview Experiences

* Morgan Stanley Interview Set 11 Campus

---

## Related Articles

* Maximum Product Subarray Set 3
* Maximum Product Subarray

---

---

Here’s a tight, interview-ready guide for **Maximum Product Subarray**.

---

## 2) Explanation + step-by-step dry run

### Key idea (Kadane-style for product)

Products behave differently from sums because:

* A **negative** flips signs (smallest negative × negative can become largest positive).
* A **zero** breaks the subarray.

So while scanning, keep two running values:

* `max_end` = maximum product of a subarray **ending at current index**
* `min_end` = minimum product of a subarray **ending at current index** (most negative)
* On a negative number, **swap** `max_end` and `min_end`.
* Update:

  * `max_end = max(x, max_end * x)`
  * `min_end = min(x, min_end * x)`
* Answer = max over all `max_end`.

This is the standard O(n), O(1) DP most interviewers expect.

#### Dry run on `arr = [-2, 6, -3, -10, 0, 2]`

Initialize: `max_end = min_end = ans = -2`

1. `x = 6`
   `x > 0` → no swap
   `max_end = max(6, -2*6=-12) = 6`
   `min_end = min(6, -12) = -12`
   `ans = max(-2, 6) = 6`

2. `x = -3`
   `x < 0` → swap ⇒ `max_end=-12`, `min_end=6`
   `max_end = max(-3, -12*-3=36) = 36`
   `min_end = min(-3, 6*-3=-18) = -18`
   `ans = max(6, 36) = 36`

3. `x = -10`
   `x < 0` → swap ⇒ `max_end=-18`, `min_end=36`
   `max_end = max(-10, -18*-10=180) = 180`
   `min_end = min(-10, 36*-10=-360) = -360`
   `ans = max(36, 180) = 180`

4. `x = 0`
   (zero breaks runs)
   `max_end = max(0, 180*0=0) = 0`
   `min_end = min(0, -360*0=0) = 0`
   `ans = max(180, 0) = 180`

5. `x = 2`
   `max_end = max(2, 0*2=0) = 2`
   `min_end = min(2, 0) = 0`
   `ans = max(180, 2) = 180` ✅

---

## 3) Python solutions (multiple interview-friendly ways)

### A) Kadane-style DP (single pass) — **most expected**

```python
"""
class Solution:
    def maxProduct(self,arr):
        # code here
"""
class Solution:
    def maxProduct(self, arr):
        """
        Kadane-style for product:
        Keep max/min products ending at current index.
        Time : O(n)  (single pass)
        Space: O(1)  (constant extra variables)
        """
        if not arr:
            return 0  # or raise

        max_end = min_end = ans = arr[0]

        for x in arr[1:]:
            if x < 0:
                # Negative flips roles: what used to be min may become max
                max_end, min_end = min_end, max_end

            # Extend or restart at x
            max_end = max(x, max_end * x)
            min_end = min(x, min_end * x)

            # Track the best seen so far
            ans = max(ans, max_end)

        return ans
```

### B) Two-pass **prefix/suffix** (simple, resilient to zeros)

Multiply left→right resetting at 0; do the same right→left. Take the max over both passes.

```python
class SolutionTwoPass:
    def maxProduct(self, arr):
        """
        Prefix & suffix scans with zero resets.
        Time : O(n)
        Space: O(1)
        """
        best = arr[0]
        prod = 1
        # left -> right
        for x in arr:
            prod = prod * x if prod != 0 else x
            best = max(best, prod)
        # right -> left
        prod = 1
        for x in reversed(arr):
            prod = prod * x if prod != 0 else x
            best = max(best, prod)
        return best
```

### C) Brute force (for completeness / sanity checks)

Compute product of every subarray; quadratic time.

```python
class SolutionBrute:
    def maxProduct(self, arr):
        """
        Brute force: all subarrays.
        Time : O(n^2)  (O(1) update per expansion)
        Space: O(1)
        """
        n = len(arr)
        best = arr[0]
        for i in range(n):
            p = 1
            for j in range(i, n):
                p *= arr[j]
                if p > best:
                    best = p
        return best
```

> In most interviews, implement **A**. If you have time, mention **B** as an alternative that’s simpler to reason about across zeros and negatives.

---

## 4) Interviewer-style Q\&A

**Q1. Why track both `max_end` and `min_end`?**
Because a **negative** value can turn the smallest (most negative) product into the largest positive when multiplied. You need both to handle sign flips.

**Q2. How do zeros affect the algorithm?**
Zero breaks any running subarray. In method A, the formulas naturally reset (`max(x, max_end*x)` with `x=0` yields 0; the next step can restart). In method B, we explicitly reset the product at zeros.

**Q3. What are the complexities?**

* DP (A): **O(n)** time, **O(1)** space.
* Two-pass (B): **O(n)** time, **O(1)** space.
* Brute (C): **O(n²)** time.

**Q4. Edge cases to test?**

* All negatives with odd/even count (e.g., `[-1, -2, -3]`, `[-1, -2, -3, -4]`)
* Contains zeros (e.g., `[0, -2, 0, -3, -4]`)
* Single element arrays
* All positives

**Q5. Can we also return the subarray indices?**
Yes: maintain temporary start indices; when you choose `x` over `max_end*x`, restart the current start at this index; when updating `ans`, record best interval. (Omitted here to keep it concise.)

**Q6. Any numerical overflow issues?**
The prompt guarantees 32-bit fits, but Python uses arbitrary-precision integers, so you’re safe in Python.

---

---

Here’s a **full, runnable Python program** for **Maximum Product Subarray** that:

* implements the **Kadane-style product DP** (O(n), O(1)),
* also includes a **two-pass prefix/suffix** variant and a **brute-force** checker,
* prints **inputs → outputs** for sample cases, and
* **benchmarks** the algorithm using `timeit` inside `main`.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Maximum Product Subarray
------------------------
Given an integer array (can include negatives and zeros), return the maximum
product of any contiguous subarray.

Main algorithm below: Kadane-style DP for products.
We track:
  - max_end: max product of a subarray ending at current index
  - min_end: min product of a subarray ending at current index
A negative value flips signs, so we swap(max_end, min_end) when x < 0.

Big-O summary:
  • Time  : O(n)   — single pass through the array
  • Space : O(1)   — constant extra variables

This script:
  1) Implements class Solution.maxProduct (Kadane-style, O(n)/O(1)).
  2) Includes a two-pass prefix/suffix variant and a brute-force checker.
  3) Prints results for sample inputs (input → output).
  4) Benchmarks the algorithms using timeit.
"""

from __future__ import annotations
import random
import timeit
from typing import List


# -----------------------------------------------------------------------------
# Primary interview solution: Kadane-style product DP (O(n) time, O(1) space)
# -----------------------------------------------------------------------------
class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        """
        Kadane-style DP for products.

        Steps (with per-step complexity):
          A) Handle empty input / init                  -> O(1)
          B) Iterate once over arr[1:]                  -> O(n)
               - If x < 0, swap(max_end, min_end)       -> O(1)
               - max_end = max(x, max_end * x)          -> O(1)
               - min_end = min(x, min_end * x)          -> O(1)
               - ans = max(ans, max_end)                -> O(1)
          C) Return ans                                  -> O(1)

        Overall:
          Time  O(n),  Space O(1)
        """
        if not arr:              # A) guard — O(1)
            return 0

        # Initialize with the first element — handles single-element arrays.
        max_end = min_end = ans = arr[0]

        # B) single pass through the rest
        for x in arr[1:]:
            if x < 0:
                # Negative flips roles: smallest may become biggest if multiplied by x
                max_end, min_end = min_end, max_end

            # Extend or restart at current value x
            max_end = max(x, max_end * x)  # best positive ending here
            min_end = min(x, min_end * x)  # worst negative ending here

            # Track global best
            if max_end > ans:
                ans = max_end

        return ans                # C)


# -----------------------------------------------------------------------------
# Alternative: Two-pass prefix/suffix (also O(n)/O(1)) — simple & robust to zeros
# -----------------------------------------------------------------------------
class SolutionTwoPass:
    def maxProduct(self, arr: List[int]) -> int:
        """
        Multiply left→right and right→left; reset at zeros.
        Time  O(n) | Space O(1)
        """
        best = arr[0]
        prod = 1
        # Left to right
        for x in arr:
            prod = prod * x if prod != 0 else x
            if prod > best:
                best = prod
        # Right to left
        prod = 1
        for x in reversed(arr):
            prod = prod * x if prod != 0 else x
            if prod > best:
                best = prod
        return best


# -----------------------------------------------------------------------------
# Brute-force checker (O(n^2) time) — for validation on small inputs
# -----------------------------------------------------------------------------
class SolutionBrute:
    def maxProduct(self, arr: List[int]) -> int:
        """
        Check every subarray product by expanding from each i.
        Time  O(n^2) | Space O(1) — for reference/testing only.
        """
        n = len(arr)
        best = arr[0]
        for i in range(n):             # O(n)
            p = 1
            for j in range(i, n):      # O(n) inner
                p *= arr[j]            # O(1) update
                if p > best:
                    best = p
        return best


# ------------------------------- Demo & Benchmark -------------------------------

def demo_on_samples() -> None:
    """
    Show correctness on the prompt's examples (and a couple extra).
    Each call runs in O(n); total here is tiny.
    """
    samples = [
        ([-2, 6, -3, -10, 0, 2], 180),
        ([-1, -3, -10, 0, 6],     30),
        ([2, 3, 4],               24),
        ([-2],                    -2),
        ([0, -2, 0, -3, -4, 0],   12),  # {-3, -4} -> 12
    ]
    sol = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for arr, expected in samples:
        out = sol.maxProduct(arr)      # O(n)
        print(f"Input    : {arr}")
        print(f"Output   : {out}")
        print(f"Expected : {expected}")
        print("-" * 60)


def _bench_kadane(arr: List[int]) -> None:
    """Timeit target for Kadane-style DP (O(n))."""
    Solution().maxProduct(arr)


def _bench_two_pass(arr: List[int]) -> None:
    """Timeit target for two-pass method (O(n))."""
    SolutionTwoPass().maxProduct(arr)


def benchmark() -> None:
    """
    Benchmark both O(n) implementations using timeit.

    Input prep (outside timing):
      - Build a random array of length N with values in [-10, 10] per constraints.
      - Ensure it's not all zeros.
    Timed region:
      - Each run: a single O(n) pass.
    """
    rng = random.Random(2025)
    N = 200_000
    vals = list(range(-10, 11))
    arr = [rng.choice(vals) for _ in range(N)]
    if all(x == 0 for x in arr):       # prevent degenerate all-zero case
        arr[rng.randrange(N)] = 1

    runs = 3
    t_k = timeit.timeit(lambda: _bench_kadane(arr), number=runs)
    t_t = timeit.timeit(lambda: _bench_two_pass(arr), number=runs)

    print("=== Benchmark (O(n) algorithms) ===")
    print(f"Array length : {N}")
    print(f"Runs         : {runs}")
    print(f"Kadane   total: {t_k:.6f} s | avg/run: {t_k / runs:.6f} s")
    print(f"Two-pass total: {t_t:.6f} s | avg/run: {t_t / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Show outputs for explicit inputs (includes the inputs and outputs)
    demo_on_samples()

    # 2) Benchmark the optimized methods with timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (short & important)

1. **Financial returns (contiguous days)**
   Daily returns multiply (compound). The maximum product subarray finds the period with **maximum compounded growth** (accounting for negative/zero returns).

2. **Signal/Audio gain chains**
   A sequence of multiplicative gains/attenuations (some < 1, some negative flips). The algorithm finds the contiguous segment with **maximum net gain**.

3. **Reliability/Probability streaks**
   When per-step success odds multiply (e.g., pipeline stages), this locates the contiguous block with **highest overall success probability** or—in log space—the largest sum.

4. **Bioinformatics/read quality**
   Consecutive read quality multipliers (or likelihood ratios) can be scanned for the subsequence with **strongest combined evidence**.

5. **Manufacturing process windows**
   Multiplicative yield factors across steps: find the **best continuous run** (e.g., shifts/machines) that maximizes product yield.
