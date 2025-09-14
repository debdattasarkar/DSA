# Trapping Rain Water

**Difficulty:** Hard
**Accuracy:** 33.14%
**Submissions:** 471K+
**Points:** 8
**Average Time:** 20m

---

## Problem Statement

Given an array `arr[]` with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season.

---

## Examples

### Example 1

**Input:** `arr[] = [3, 0, 1, 0, 4, 0, 2]`
**Output:** `10`
**Explanation:** Total water trapped = `0 + 3 + 2 + 3 + 0 + 2 + 0 = 10` units.

### Example 2

**Input:** `arr[] = [3, 0, 2, 0, 4]`
**Output:** `7`
**Explanation:** Total water trapped = `0 + 3 + 1 + 3 + 0 = 7` units.

### Example 3

**Input:** `arr[] = [1, 2, 3, 4]`
**Output:** `0`
**Explanation:** We cannot trap water as there is no height bound on both sides.

### Example 4

**Input:** `arr[] = [2, 1, 5, 3, 1, 0, 4]`
**Output:** `9`
**Explanation:** Total water trapped = `0 + 1 + 0 + 1 + 3 + 4 + 0 = 9` units.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `0 ≤ arr[i] ≤ 10^3`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Flipkart, Amazon, Microsoft, Google, Goldman Sachs

---

## Topic Tags

Arrays, Data Structures, Algorithms, Stack, two-pointer-algorithm

---

## Related Interview Experiences

* Payu Interview On Campus
* Accolite Interview Experience Set 13 On Campus For Internship And FTE
* Amazon Interview Experience 219 On Campus

---

## Related Articles

* [Trapping Rain Water](https://www.geeksforgeeks.org/trapping-rain-water/)

---

---

here’s an interview-ready breakdown for **Trapping Rain Water**.

---

# 2) Explanation + step-by-step dry run

## Core idea

Water above bar `i` is limited by the **shorter** of the tallest walls on its **left** and **right**:

```
water[i] = max( min(leftMax[i], rightMax[i]) - arr[i], 0 )
```

We can compute this in several ways. The most common O(1)-space approach uses **two pointers** that keep running maxima from both ends.

### Two-pointer intuition

Maintain:

* `l`, `r` — left/right indices
* `leftMax`, `rightMax` — tallest bars seen so far from the left/right

Invariant: the side with the **smaller current max** determines the water level there, because on that side the opposite boundary cannot improve it.
So:

* If `leftMax ≤ rightMax`, water at `l` is `leftMax - arr[l]` (if positive), then move `l++`.
* Else handle the right side symmetrically and move `r--`.

### Dry run on `arr = [3, 0, 1, 0, 4, 0, 2]` (answer = 10)

|                                     step | l,r | leftMax | rightMax |                                 action                                | added | total |
| ---------------------------------------: | :-: | :-----: | :------: | :-------------------------------------------------------------------: | :---: | :---: |
|                                     init | 0,6 |    3    |     2    | right side smaller? no → **left ≤ right**? 3 ≤ 2 false ⇒ handle right |   —   |   0   |
| Since `rightMax < leftMax`, process `r`: |     |         |          |                                                                       |       |       |

* r=6: water = `rightMax - arr[6] = 2-2=0`, r→5, rightMax=max(2,0)=2, total=0
* r=5: water = `2-0=2`, **+2**, r→4, rightMax=max(2,4)=4, total=2
  Now `leftMax(3) ≤ rightMax(4)`, process left:
* l=0: water = `3-3=0`, l→1, leftMax=max(3,0)=3, total=2
* l=1: `min side == left` → water = `3-0=3`, **+3**, l→2, leftMax=3, total=5
* l=2: water = `3-1=2`, **+2**, l→3, leftMax=3, total=7
* l=3: water = `3-0=3`, **+3**, l→4, leftMax=max(3,0)=3, total=10
  Now l=4, r=4 (stop).
  Total trapped = **10**.

(Equivalent per-index sum in the statement: `0 + 3 + 2 + 3 + 0 + 2 + 0 = 10`.)

---

# 3) Python solutions (brute + optimized, with inline comments)

```python
class Solution:
    def maxWater(self, arr):
        """
        Two-pointer optimized solution (most expected in interviews)
        Time:  O(n)  - each index visited at most once
        Space: O(1)  - constant extra space
        """
        n = len(arr)
        if n < 3:                      # Need at least 3 bars to trap water
            return 0

        l, r = 0, n - 1                # O(1)
        leftMax, rightMax = arr[l], arr[r]
        water = 0

        # Single pass: O(n)
        while l < r:
            # Decide by smaller boundary (it caps the water on that side)
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, arr[l])
                # if leftMax > arr[l], we trap leftMax - arr[l] units at l
                water += max(0, leftMax - arr[l])
            else:
                r -= 1
                rightMax = max(rightMax, arr[r])
                water += max(0, rightMax - arr[r])

        return water
```

### Prefix–Suffix maxima (clear & fast; O(n) time, **O(n) space**)

```python
class SolutionPrefixSuffix:
    def maxWater(self, arr):
        """
        Precompute leftMax[i] and rightMax[i], then sum:
          water[i] = max(min(leftMax[i], rightMax[i]) - arr[i], 0)
        Time:  O(n)
        Space: O(n)
        """
        n = len(arr)
        if n < 3:
            return 0

        leftMax = [0] * n
        rightMax = [0] * n

        # Build leftMax: O(n)
        leftMax[0] = arr[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], arr[i])

        # Build rightMax: O(n)
        rightMax[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], arr[i])

        # Sum water at each index: O(n)
        ans = 0
        for i in range(n):
            ans += max(0, min(leftMax[i], rightMax[i]) - arr[i])
        return ans
```

### Monotonic stack (traps water when a “right wall” closes a basin)

```python
class SolutionStack:
    def maxWater(self, arr):
        """
        Use a stack of indices with non-increasing heights.
        When current height > height[stack[-1]], pop to form a container
        bounded by current index and new stack top.
        Time:  O(n)   - each index pushed/popped at most once
        Space: O(n)
        """
        n = len(arr)
        st = []
        water = 0

        for i, h in enumerate(arr):
            # While current bar is a right boundary higher than the basin floor
            while st and h > arr[st[-1]]:
                bottom = st.pop()
                if not st:  # no left wall
                    break
                left = st[-1]
                width = i - left - 1
                bounded_height = min(arr[left], h) - arr[bottom]
                if bounded_height > 0:
                    water += width * bounded_height
            st.append(i)
        return water
```

### Brute force (for completeness / baseline)

```python
class SolutionBrute:
    def maxWater(self, arr):
        """
        For each i, scan left/right to find max on both sides, then add.
        Time:  O(n^2)  - two scans per index
        Space: O(1)
        """
        n = len(arr)
        ans = 0
        for i in range(n):
            left = 0
            for L in range(i + 1):          # max to the left including i
                left = max(left, arr[L])
            right = 0
            for R in range(i, n):           # max to the right including i
                right = max(right, arr[R])
            ans += max(0, min(left, right) - arr[i])
        return ans
```

---

# 4) Interviewer-style Q\&A

**Q1. Why does the two-pointer method work?**
Because the trapped water at a position depends on the **smaller** of the max walls on both sides. If `leftMax ≤ rightMax`, the water level on the left is fixed at `leftMax` regardless of anything to the right, so we can finalize `l` and move `l++`. Symmetric for the right side.

**Q2. When would you prefer prefix/suffix arrays?**
When clarity matters more than space or when you might need `leftMax[i]`/`rightMax[i]` later (e.g., to print per-index water). It’s still linear time but uses `O(n)` space.

**Q3. What’s the stack approach intuition?**
Maintain a **non-increasing** stack of indices. When you meet a bar taller than the top, you’ve closed a basin: pop the bottom, and compute water using the min of the new left wall and current bar, times the horizontal width.

**Q4. Edge cases?**

* `n < 3` → `0`.
* Monotone non-decreasing or non-increasing arrays → `0`.
* Equal heights are fine; comparisons use `≤` where appropriate.

**Q5. What about integer overflow?**
In Python you’re safe. In languages with fixed widths, use 64-bit (`long long`) because accumulated water can be large (`≤ 10^5 * 10^3` in typical constraints).

**Q6. Variations?**

* **Variable bar widths**: multiply each local water height by the corresponding width.
* **2D (Trapping Rain Water II)**: use a min-heap (Dijkstra-like expansion from the boundary).

**Q7. Why not compute `min(leftMax, rightMax)` on the fly per index?**
You’d still need a right scan for each index → `O(n^2)`. Two-pointer or prefix/suffix avoids that.

---

---

Here’s a **full, runnable Python program** for **Trapping Rain Water** that:

* prints outputs for several **input arrays** (input → output),
* includes **inline time & space complexity notes for every step**, and
* **benchmarks** the optimized solution using `timeit` right inside `main`.

```python
#!/usr/bin/env python3
"""
Trapping Rain Water
Given non-negative bar heights (width = 1 each), compute total trapped water.

Core interview solution: Two-pointers with running left/right maxima.
Why it works: the water level at a side is capped by the smaller boundary.
If leftMax <= rightMax, the left side's water is decided (can't be raised by right),
so we finalize water at 'l' and move l++. Symmetric for the right.

Complexities:
- Two-pointers: Time O(n), Space O(1)
- Prefix/Suffix maxima (reference): Time O(n), Space O(n)
- Stack method (reference): Time O(n), Space O(n)

This script:
  1) Implements the optimized O(n)/O(1) method in class Solution (signature as requested).
  2) Also provides prefix-suffix and stack variants for reference.
  3) Prints results for sample inputs (input values + output).
  4) Benchmarks the optimized method using timeit.
"""

from __future__ import annotations
import random
import timeit
from typing import List


class Solution:
    def maxWater(self, arr: List[int]) -> int:
        """
        Two-pointer optimized solution (most expected in interviews).

        Steps:
          A) Handle trivial length (<3) → no trapping possible.
             Time:  O(1)     Space: O(1)
          B) Initialize l, r pointers and leftMax, rightMax.
             Time:  O(1)     Space: O(1)
          C) Single pass while l < r:
               - If leftMax <= rightMax:
                    move l right; update leftMax; add max(0, leftMax - arr[l])
                 else:
                    move r left;  update rightMax; add max(0, rightMax - arr[r])
             Time:  O(n)     Space: O(1)
          D) Return accumulated water.
             Time:  O(1)     Space: O(1)

        Overall: Time O(n), Space O(1)
        """
        n = len(arr)
        if n < 3:                       # A) O(1)/O(1)
            return 0

        # B) O(1)/O(1)
        l, r = 0, n - 1
        leftMax, rightMax = arr[l], arr[r]
        water = 0

        # C) O(n)/O(1)
        while l < r:
            if leftMax <= rightMax:
                l += 1
                # update running max from the left — O(1)
                leftMax = leftMax if leftMax >= arr[l] else arr[l]
                # water at l is bounded by leftMax (since rightMax >= leftMax) — O(1)
                trapped = leftMax - arr[l]
                if trapped > 0:
                    water += trapped
            else:
                r -= 1
                # update running max from the right — O(1)
                rightMax = rightMax if rightMax >= arr[r] else arr[r]
                trapped = rightMax - arr[r]
                if trapped > 0:
                    water += trapped

        # D) O(1)/O(1)
        return water


# -------- Optional reference implementations (not used in the benchmark) -------- #

class SolutionPrefixSuffix:
    def maxWater(self, arr: List[int]) -> int:
        """
        Prefix/Suffix maxima method.
        Time:  O(n)   (3 linear passes)
        Space: O(n)   (two arrays)
        """
        n = len(arr)
        if n < 3:
            return 0

        left = [0] * n
        right = [0] * n

        # Build left max — O(n)/O(n)
        left[0] = arr[0]
        for i in range(1, n):
            left[i] = left[i - 1] if left[i - 1] >= arr[i] else arr[i]

        # Build right max — O(n)/O(n)
        right[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] if right[i + 1] >= arr[i] else arr[i]

        # Sum water — O(n)/O(1) extra
        ans = 0
        for i in range(n):
            cap = left[i] if left[i] <= right[i] else right[i]
            fill = cap - arr[i]
            if fill > 0:
                ans += fill
        return ans


class SolutionStack:
    def maxWater(self, arr: List[int]) -> int:
        """
        Monotonic stack (indices of non-increasing heights).
        Time:  O(n)   (each index pushed/popped at most once)
        Space: O(n)
        """
        water = 0
        st: List[int] = []

        for i, h in enumerate(arr):
            while st and h > arr[st[-1]]:
                bottom = st.pop()
                if not st:                 # no left boundary
                    break
                left = st[-1]
                width = i - left - 1
                bounded = min(arr[left], h) - arr[bottom]
                if bounded > 0:
                    water += width * bounded
            st.append(i)
        return water


# ------------------------------ Demo & Benchmark ------------------------------ #

def demo_on_samples() -> None:
    """
    Print results for several inputs (input → output) using all variants.
    Total time for this function is proportional to the total input size.
    Extra space is O(1) besides local variables.
    """
    samples = [
        [3, 0, 1, 0, 4, 0, 2],      # expected 10
        [3, 0, 2, 0, 4],            # expected 7
        [1, 2, 3, 4],               # expected 0
        [2, 1, 5, 3, 1, 0, 4],      # expected 9
        [0, 0, 0],                  # expected 0
    ]

    tp = Solution()
    ps = SolutionPrefixSuffix()
    st = SolutionStack()

    print("=== Sample Runs (Input → Output) ===")
    for arr in samples:
        arr1 = list(arr)
        arr2 = list(arr)
        arr3 = list(arr)
        out_tp = tp.maxWater(arr1)     # O(n)/O(1)
        out_ps = ps.maxWater(arr2)     # O(n)/O(n)
        out_st = st.maxWater(arr3)     # O(n)/O(n)
        print(f"Input : {arr}")
        print(f"Two-pointers    (O(n)/O(1)) -> {out_tp}")
        print(f"Prefix/Suffix   (O(n)/O(n)) -> {out_ps}")
        print(f"Monotonic Stack (O(n)/O(n)) -> {out_st}")
        print("-" * 60)


def _bench_once(arr: List[int]) -> None:
    """
    Helper for timeit: runs only the optimized algorithm.
    The algorithm does not modify the list, so we can reuse the same array.
    """
    Solution().maxWater(arr)


def benchmark() -> None:
    """
    Benchmark the optimized two-pointer solution using timeit.

    Prep (outside timed region):
      - Generate a random array 'arr' of size SIZE with heights in [0, MAXH].
        Time:  O(SIZE), Space: O(SIZE)

    Timed region:
      - Each run executes O(n) time / O(1) space algorithm over the same array.
    """
    SIZE = 200_000
    MAXH = 1000
    rng = random.Random(99)

    # Build input once (not timed): O(n) time / O(n) space
    arr = [rng.randrange(0, MAXH + 1) for _ in range(SIZE)]

    runs = 3
    total = timeit.timeit(lambda: _bench_once(arr), number=runs)

    print("=== Benchmark (Two-pointers O(n)/O(1)) ===")
    print(f"Array size : {SIZE}")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f} s")
    print(f"Avg / run  : {total / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Show outputs for concrete inputs
    demo_on_samples()

    # 2) Benchmark the optimized method
    benchmark()


if __name__ == "__main__":
    main()
```

---

## Real-World Use Cases (short, high-value)

1. **Urban drainage / roof gutter sizing (1D cross-section):**
   Estimate water pooling between obstacles/walls along a street or gutter profile to check **accumulation hot spots** in a simplified cross-section.

2. **Chip manufacturing & microfluidic channels:**
   In narrow trenches/channels, compute **retained fluid volume** between features for process design or cleaning rinse coverage.

3. **Landscape & site grading along a transect:**
   For a 1D elevation cut, identify **depressions** that will hold water after rainfall, informing grading or drainage placement.

