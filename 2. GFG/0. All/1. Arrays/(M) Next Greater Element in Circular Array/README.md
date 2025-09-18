# Next Greater Element in Circular Array

**Difficulty:** Medium
**Accuracy:** 56.97%
**Submissions:** 48K+
**Points:** 4

---

## Problem Statement

Given a circular integer array `arr[]`, the task is to determine the next greater element (**NGE**) for each element in the array.

The **next greater element** of an element `arr[i]` is the first element that is greater than `arr[i]` when traversing **circularly**. If no such element exists, return `-1` for that position.

### Circular Property

Since the array is circular, after reaching the last element, the search continues from the beginning until we have looked at all elements once.

---

## Examples

### Example 1

**Input:** `arr[] = [1, 3, 2, 4]`
**Output:** `[3, 4, 4, -1]`
**Explanation:**

* The next greater element for `1` is `3`.
* The next greater element for `3` is `4`.
* The next greater element for `2` is `4`.
* The next greater element for `4` does not exist, so return `-1`.

---

### Example 2

**Input:** `arr[] = [0, 2, 3, 1, 1]`
**Output:** `[2, 3, -1, 2, 2]`
**Explanation:**

* The next greater element for `0` is `2`.
* The next greater element for `2` is `3`.
* The next greater element for `3` does not exist, so return `-1`.
* The next greater element for `1` is `2` (from circular traversal).
* The next greater element for `1` is `2` (from circular traversal).

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `0 ≤ arr[i] ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Flipkart, Amazon, Microsoft

---

## Topic Tags

Stack, Data Structures

---

## Related Interview Experiences

* Flipkart Interview Experience For SDE Internship 2021

---

## Related Articles

* Find The Next Greater Element In A Circular Array
* Next Greater Element

---

---

Here’s a tight, interview-ready package for **Next Greater Element in a Circular Array**.

---

## 2) Intuition + step-by-step dry run

### What we need

For each `arr[i]`, find the **first element to its right (wrapping around)** that is strictly greater. If none exists, return `-1`.

### Key idea (monotonic stack)

Traverse the array **twice** (to simulate circularity) while maintaining a stack of **indices whose NGE is not found yet**. Keep the stack **monotonically decreasing by value** (top holds the **latest, smallest** candidate).
Whenever the current value is greater than the value at the stack top, we’ve found the next greater for that top.

Why it’s O(n): each index is **pushed once and popped at most once**.

### Dry run

`arr = [1, 3, 2, 4]` (n = 4)
Initialize `ans = [-1, -1, -1, -1]`, `st = []` (stack of indices)

Loop i from `0 .. 2n-1 = 7`, let `j = i % n`:

* i=0, j=0, val=1
  stack empty → push 0 → st=\[0]
* i=1, j=1, val=3
  arr\[1]=3 > arr\[0]=1 → pop 0, set ans\[0]=3 → st=\[]
  push 1 → st=\[1]
* i=2, j=2, val=2
  2 ≤ arr\[1]=3 → push 2 → st=\[1,2]
* i=3, j=3, val=4
  4 > arr\[2]=2 → pop 2, ans\[2]=4
  4 > arr\[1]=3 → pop 1, ans\[1]=4
  push 3 → st=\[3]
* i=4, j=0, val=1 (second lap)
  1 ≤ arr\[3]=4 → don’t resolve; **don’t push (optional)** or you may push if using the “push only in first lap” variant.
* i=5, j=1, val=3  (second lap)
  3 ≤ 4 → nothing
* i=6, j=2, val=2  (second lap)
  2 ≤ 4 → nothing
* i=7, j=3, val=4  (second lap)
  4 ≤ 4 → nothing

`ans = [3, 4, 4, -1]`.

---

## 3) Python solutions

### A) Optimal O(n) time, O(n) space — stack, two passes (most expected)

```python
class Solution:
    def nextGreater(self, arr):
        """
        Monotonic stack over two passes (simulate circular array):
        - Time : O(n)  (each index pushed and popped at most once)
        - Space: O(n)  (stack + output)
        """
        n = len(arr)
        ans = [-1] * n
        st = []  # stack of indices whose NGE we haven't found yet

        # Traverse twice; only push indices from the first pass
        for i in range(2 * n):
            j = i % n
            # Resolve as long as current value is greater than stack top
            while st and arr[j] > arr[st[-1]]:
                ans[st.pop()] = arr[j]
            # Push only during the first pass so each index is pushed once
            if i < n:
                st.append(j)
        return ans
```

### B) Optimal O(n) time — reverse scan variant (clean & popular)

Scan from right to left over `2n` positions; keep a decreasing stack of **values** (or indices). This one avoids “push only in first pass” logic.

```python
class Solution:
    def nextGreater(self, arr):
        """
        Reverse over 2n-1..0. Stack holds candidate values (strictly decreasing).
        - Time : O(n)
        - Space: O(n)
        """
        n = len(arr)
        ans = [-1] * n
        st = []  # stack of values that could be next greater

        # Go backwards so the stack already has the "right" side candidates
        for i in range(2 * n - 1, -1, -1):
            j = i % n
            # Maintain decreasing stack: pop <= current
            while st and st[-1] <= arr[j]:
                st.pop()
            if i < n:
                ans[j] = st[-1] if st else -1
            st.append(arr[j])
        return ans
```

### C) Brute force O(n²) — simple but slow (good to mention, not to use)

For each i, walk up to n-1 steps circularly until finding a greater one.

```python
class Solution:
    def nextGreater(self, arr):
        """
        Brute force:
        - Time : O(n^2)
        - Space: O(1) extra (besides output)
        """
        n = len(arr)
        ans = [-1] * n
        for i in range(n):
            for k in range(1, n):               # at most n-1 steps
                j = (i + k) % n
                if arr[j] > arr[i]:
                    ans[i] = arr[j]
                    break
        return ans
```

> In interviews, code **A** or **B**. Explain correctness (monotonic invariant + circularity via 2 passes) and O(n) bound (each index/value pushed/popped at most once).

---

## 4) Interviewer-style Q\&A

**Q1. Why does the monotonic stack guarantee O(n) time?**
Each index enters the stack once and leaves once. The `while` loop across the whole algorithm pops each index at most once, hence total pops ≤ n and total operations are linear.

**Q2. How do you handle the circular nature?**
By iterating **2n** elements using `% n`, you let every position “see” elements to its right and the wrap-around elements. In variant A, we push indices only in the **first pass** to avoid duplicates; the second pass only resolves pending items. In variant B, we fill answers when `i < n` and still use the full 2n sweep to pre-load right candidates.

**Q3. What about duplicates or equal elements?**
We need *strictly* greater. Thus, while maintaining the decreasing stack, we pop while `<= current`. Equal elements do **not** count as next greater.

**Q4. Edge cases?**

* Single element → `[-1]`.
* Strictly decreasing array → all `-1`.
* All equal → all `-1`.
* Very large values (up to 1e6) — no issue; algorithm depends on comparisons, not value range.

**Q5. Can we do it in-place?**
You still need the `ans` array; the stack can store indices. In Python, “in-place” beyond that provides no practical gain and can reduce clarity.

**Q6. Why forward two-pass vs reverse scan?**
Both are O(n). The forward two-pass method naturally mirrors the problem statement; the reverse scan can feel elegant because the stack always represents “things to the right” at each step.

---

---

Here’s a complete, runnable program for **Next Greater Element in a Circular Array** with:

* The required `class Solution.nextGreater(self, arr)` method
* Inline **time/space complexity** notes where the work happens
* Sample **inputs → outputs**
* A small **timeit** benchmark for the whole run

---

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Next Greater Element in a Circular Array

Given arr (length n), for each i return the first element strictly greater than
arr[i] encountered while moving right *circularly*; else -1.

Overall target complexities for the optimal stack approach:
  Time  : O(n)          (each index pushed & popped at most once)
  Space : O(n)          (answer array + stack of up to n indices)
"""

from __future__ import annotations
import random
import timeit
from typing import List


# ============================================================
# Core Solution (forward 2-pass monotonic stack) — MOST USED
# ============================================================
class Solution:
    def nextGreater(self, arr: List[int]) -> List[int]:
        """
        Monotonic stack + 2 passes to simulate circular traversal.

        Steps & complexities:
          1) n = len(arr)                                 -> O(1) time, O(1) space
          2) ans = [-1] * n, st = [] (stack of indices)   -> O(n) time to init ans, O(n) space
          3) for i in range(2*n):                          -> O(2n) iterations (linear)
               j = i % n                                   -> O(1)
               while st and arr[j] > arr[st[-1]]:          -> Each index popped once total => O(n) amortized
                   ans[st.pop()] = arr[j]
               if i < n:                                   -> Push each index once
                   st.append(j)

        Net:
          Time  : O(n)   (push ≤ n, pop ≤ n, loop 2n is still linear)
          Space : O(n)   (ans + stack)
        """
        n = len(arr)
        ans = [-1] * n  # O(n) space
        st: List[int] = []

        # 2 passes: indices are only *pushed* in the first pass
        for i in range(2 * n):                # O(2n) ~ O(n)
            j = i % n
            # Resolve all indices whose next greater is arr[j]
            while st and arr[j] > arr[st[-1]]:  # Every index pops at most once => O(n) total
                ans[st.pop()] = arr[j]
            if i < n:                          # Push each index exactly once
                st.append(j)
        return ans


# -------------------------------------------
# (Optional) A simple O(n^2) brute for sanity
# -------------------------------------------
def brute_next_greater_circular(arr: List[int]) -> List[int]:
    n = len(arr)
    res = [-1] * n
    for i in range(n):                    # O(n)
        for k in range(1, n):             # worst O(n) per i
            j = (i + k) % n
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break
    return res  # Total O(n^2), O(1) extra space


# ===================
# Demo: sample inputs
# ===================
def demo() -> None:
    sol = Solution()
    samples = [
        [1, 3, 2, 4],          # -> [3, 4, 4, -1]
        [0, 2, 3, 1, 1],       # -> [2, 3, -1, 2, 2]
        [5],                   # -> [-1]
        [4, 3, 2, 1],          # decreasing -> [-1, -1, -1, -1]
        [2, 2, 2],             # equal -> [-1, -1, -1]
        [1, 5, 3, 6, 8],       # -> [5, 6, 6, 8, -1]
    ]

    print("=== Sample Runs ===")
    for arr in samples:
        print(f"in : {arr}")
        out = sol.nextGreater(arr[:])
        print(f"out: {out}")
        # (Optional) sanity check for small arrays:
        if len(arr) <= 10:
            assert out == brute_next_greater_circular(arr), "Mismatch vs brute!"
        print("-" * 48)


# =========================
# Benchmark with timeit
# =========================
def _bench_once(size: int, seed: int = 42) -> None:
    random.seed(seed)
    # Build a random array with values in a reasonable range
    arr = [random.randint(0, 10**6) for _ in range(size)]
    sol = Solution()
    sol.nextGreater(arr)  # measure the full function call

def benchmark() -> None:
    sizes = [1_000, 5_000, 10_000, 20_000]   # adjust if you need faster/slower runs
    runs = 3

    print("=== Benchmark (timeit) ===")
    for n in sizes:
        total = timeit.timeit(lambda: _bench_once(n), number=runs)
        print(f"n={n:>6} | runs={runs} | total={total:.4f}s | avg/run={total/runs:.4f}s")
    print("-" * 48)


# =============
# Main driver
# =============
def main() -> None:
    demo()
    benchmark()

if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (high-impact)

1. **Monitoring / Alerting Windows (Circular Dashboards):**
   In rotating dashboards or ring buffers of sensor metrics, quickly find the **next higher reading** for a datapoint when scanning circularly (e.g., next spike after this time, wrapping to start).

2. **Cyclic Schedules & Rotas:**
   In shift-planning or round-robin tournament tables, find the **next longer (or more critical) task** after a given slot, cycling across days/weeks.

3. **Stock/Ticker Rings & Stream Windows:**
   For a circular window of last N ticks, compute for each price the **next larger price** ahead, used in technical signals (e.g., where is the next breakout relative to a point in the window).

4. **Networking / Token Ring Protocols:**
   In ring-topology simulations, for each node’s metric (load, priority), determine the **next node with a higher threshold** scanning clockwise.

5. **Game Development (Circular Tracks/Maps):**
   On circular tracks, for each checkpoint’s difficulty value, find the **next higher difficulty** ahead (used in pacing/AI decisions).
